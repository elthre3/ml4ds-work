#!/usr/bin/env python3
"""Derive the student notebook from the teacher (_complete) one.

Usage:  make_incomplete.py <complete.qmd> <student.qmd>
        make_incomplete.py --solutions <complete.qmd> <solutions.qmd>
        make_incomplete.py --instructor <complete.qmd> <instructor.qmd>
        make_incomplete.py --solutions-hash <complete.qmd>   (prints the sha256 of what --solutions would write)
        make_incomplete.py --check <complete.qmd>      (marker balance only)

Three documents come from the one source (convenor, 8 October 2026). The
teacher's notebook is the _complete file itself, published for seminar teachers
only. The student notebook is that file without its answers. The notebook with
solutions is what students are given the week after the seminar: a separate
document, so that the two can differ. For now it is the complete notebook
without the teacher-only comment at the top; what else differs is to be
decided, and derive_solutions() below is the place for it.

A fourth document, the instructor notebook, is made only from a complete notebook
that has short-answer twins (convenor, 18 November 2026; week 8 first). It is
what the seminar teacher shows on the projector: the same questions, hints and
solution code, with short answers in place of the full ones. Markers:
  ::: {.callout-tip .answer .full collapse="true" title="Reveal answer"}
      A full answer: shown in the complete notebook and the notebook with
      solutions, dropped from the instructor notebook.
  ::: {.content-hidden .answer .brief}            (optionally title="...")
      Its short twin, next to it: Quarto hides it in the complete notebook,
      the notebook with solutions drops it, and the instructor notebook shows it
      as a collapsed callout titled "Reveal answer" (or the title given). A chunk
      that both answers need goes in each: in the twin with `#| include: false`,
      since the notebook with solutions drops the twin and the instructor
      notebook drops the full answer.
  <!-- not in the instructor notebook: from here -->
  <!-- not in the instructor notebook: to here -->
      Everything between is dropped from the instructor notebook (the optional
      at-home items, say); the two lines are dropped from every other document.
Both kinds of twin carry `.answer`, so the student notebook loses them as it
loses every answer. A notebook without twins or markers gives exactly what it
gave before (its stored notebook with solutions keeps its hash).

Revised 26 September 2026 for the 2026-27 seminar format: the teacher file
carries every answer in a collapsible callout that the seminar teacher opens on
screen, and the student file is the teacher file with those callouts removed.

Markers in the complete file:
  ::: {.callout-tip .answer collapse="true" title="Reveal answer"}
  ...
  :::
      Any fenced div whose opening line carries the class `.answer` is removed
      entirely, up to the next line consisting of `:::` alone. Answer divs must
      not nest other fenced divs. Prose answers ("Reveal answer") and solution
      code chunks ("Reveal solution") use the same marker.
  <details><summary>Hint ...</summary> ... </details>
      Kept as they are (collapsed in both renders).

Everything else is copied verbatim. Skeleton chunks mark the place for the
student's code with a commented line `# ...` (from 7 October 2026; a bare `...`
is still recognized), so there is no line to delete. They already carry
`#| eval: false` in the complete file (so that the teacher render does not
evaluate them either); the generator adds it where it is missing. The YAML title loses its " (complete)" suffix, and the teacher-only
HTML comment at the top is dropped. The script exits non-zero if an answer div
is opened and never closed.
"""
import sys, re

NOTICE = (
    "::: {.callout-note}\n"
    "This is the student version of the notebook. The code you write goes where "
    "a line says `# ...` or has a `____`. "
    "A code chunk with a blank starts with `#| eval: false`, so the file "
    "renders as it stands; delete that line once you have filled the blank. "
    "Working through the chunks one at a time in RStudio (Ctrl/Cmd+Enter) is "
    "unaffected. Answers are revealed in the seminar.\n"
    ":::\n"
)

OPEN = re.compile(r"^:::+\s*\{[^}]*\.answer[^}]*\}\s*$")
BRIEF = re.compile(r"^:::+\s*\{[^}]*\.brief\b[^}]*\}\s*$")
FULL = re.compile(r"^:::+\s*\{[^}]*\.full\b[^}]*\}\s*$")
OMIT_FROM = "<!-- not in the instructor notebook: from here -->"
OMIT_TO = "<!-- not in the instructor notebook: to here -->"
BLANK = re.compile(r"^[ \t]*(#[ \t]*)?\.\.\.[ \t]*$", flags=re.M)
CLOSE = re.compile(r"^:::+\s*$")

def check_markers(txt, name):
    problems = []
    lines = txt.split("\n")
    open_at = None
    for i, line in enumerate(lines, 1):
        if OPEN.match(line):
            if open_at is not None:
                problems.append(f"{name}: answer div opened at line {open_at} not closed before line {i}")
            open_at = i
        elif CLOSE.match(line) and open_at is not None:
            open_at = None
    if open_at is not None:
        problems.append(f"{name}: answer div opened at line {open_at} never closed")
    if "ANSWER" in txt:
        problems.append(f"{name}: legacy 'ANSWER' marker found; this generator uses .answer divs")
    n_brief = n_full = 0
    omitting = None
    for i, line in enumerate(lines, 1):
        if BRIEF.match(line) or FULL.match(line):
            if not OPEN.match(line):
                problems.append(f"{name}: line {i}: a .brief or .full div must also carry .answer")
            n_brief += bool(BRIEF.match(line))
            n_full += bool(FULL.match(line))
        if line.strip() == OMIT_FROM:
            if omitting is not None:
                problems.append(f"{name}: line {i}: instructor omission opened again before line {omitting}'s was closed")
            omitting = i
        elif line.strip() == OMIT_TO:
            if omitting is None:
                problems.append(f"{name}: line {i}: instructor omission closed but never opened")
            omitting = None
    if omitting is not None:
        problems.append(f"{name}: instructor omission opened at line {omitting} never closed")
    if n_brief != n_full:
        problems.append(f"{name}: {n_full} .full answers but {n_brief} .brief twins")
    return problems

def drop_divs(txt, opener):
    """Remove every fenced div whose opening line matches opener, up to the next line of colons alone."""
    out, skipping, removed = [], False, False
    for line in txt.split("\n"):
        if not skipping and opener.match(line):
            skipping = removed = True
            continue
        if skipping:
            if CLOSE.match(line):
                skipping = False
            continue
        out.append(line)
    return "\n".join(out), removed

def drop_omit_markers(txt):
    """Remove the two marker lines, keeping what is between them."""
    lines = txt.split("\n")
    kept = [l for l in lines if l.strip() not in (OMIT_FROM, OMIT_TO)]
    return "\n".join(kept), len(kept) != len(lines)

def derive_instructor(txt):
    """The instructor notebook: short answers in place of the full ones, omitted parts dropped."""
    txt, _ = drop_divs(txt, FULL)
    out, omitting = [], False
    for line in txt.split("\n"):
        if line.strip() == OMIT_FROM:
            omitting = True
            continue
        if line.strip() == OMIT_TO:
            omitting = False
            continue
        if omitting:
            continue
        if BRIEF.match(line):
            m = re.search(r'title="([^"]*)"', line)
            line = '::: {.callout-tip collapse="true" title="%s"}' % (m.group(1) if m else "Reveal answer")
        out.append(line)
    txt = "\n".join(out)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    txt = txt.replace(" (complete)", " (instructor)", 1)
    txt = re.sub(r"(---\n.*?\n---\n)\s*<!-- Teacher version\..*?-->\n", r"\1", txt, count=1, flags=re.S)
    return txt

def derive_solutions(txt):
    """The notebook with solutions, for students. Full answers are kept, short twins dropped."""
    # teacher-only comment immediately after the YAML header
    txt = re.sub(r"(---\n.*?\n---\n)\s*<!-- Teacher version\..*?-->\n", r"\1", txt, count=1, flags=re.S)
    txt, dropped = drop_divs(txt, BRIEF)
    txt, unmarked = drop_omit_markers(txt)
    if dropped or unmarked:
        txt = re.sub(r"\n{3,}", "\n\n", txt)
    return txt

def derive(txt):
    txt, _ = drop_omit_markers(txt)
    out, skipping = [], False
    for line in txt.split("\n"):
        if not skipping and OPEN.match(line):
            skipping = True
            continue
        if skipping:
            if CLOSE.match(line):
                skipping = False
            continue
        out.append(line)
    txt = "\n".join(out)
    # collapse runs of blank lines left by removed divs
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    # title suffix
    txt = txt.replace(" (complete)", "", 1).replace("(complete)", "", 1)
    # teacher-only comment immediately after the YAML header
    txt = re.sub(r"(---\n.*?\n---\n)\s*<!-- Teacher version\..*?-->\n", r"\1", txt, count=1, flags=re.S)
    # chunks that contain a blank do not evaluate in the student render
    def chunk_repl(m):
        fence, body, close = m.group(1), m.group(2), m.group(3)
        has_blank = BLANK.search(body) is not None
        has_eval = re.search(r"^#\|\s*eval\s*:", body, flags=re.M) is not None
        if has_blank and not has_eval:
            body = "#| eval: false\n" + body
        return fence + body + close
    txt = re.sub(r"(^```\{r[^\n]*\}\n)(.*?)(^```[ \t]*$\n?)", chunk_repl, txt, flags=re.S | re.M)
    # notice after the YAML header
    m = re.match(r"---\n.*?\n---\n", txt, flags=re.S)
    if m:
        txt = txt[:m.end()] + "\n" + NOTICE + txt[m.end():]
    return txt

if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--check":
        src = args[1]
        problems = check_markers(open(src).read(), src)
        for p in problems:
            print(p, file=sys.stderr)
        sys.exit(1 if problems else 0)
    if args and args[0] == "--solutions-hash":
        # The build stores each rendered notebook with solutions next to this hash of its source,
        # and check compares the two: a stored page whose hash differs is older than the complete
        # notebook it was made from.
        import hashlib
        print(hashlib.sha256(derive_solutions(open(args[1]).read()).encode("utf-8")).hexdigest())
        sys.exit(0)
    if args and args[0] == "--instructor":
        src, dst = args[1], args[2]
        txt = open(src).read()
        problems = check_markers(txt, src)
        if not any(BRIEF.match(l) for l in txt.split("\n")):
            problems.append(f"{src}: no .brief twins, so no instructor notebook")
        if problems:
            for p in problems:
                print(p, file=sys.stderr)
            sys.exit(1)
        out = derive_instructor(txt)
        open(dst, "w").write(out)
        print(f"wrote {dst}: {sum(bool(BRIEF.match(l)) for l in txt.split(chr(10)))} short answers")
        sys.exit(0)
    if args and args[0] == "--solutions":
        src, dst = args[1], args[2]
        txt = open(src).read()
        problems = check_markers(txt, src)
        if problems:
            for p in problems:
                print(p, file=sys.stderr)
            sys.exit(1)
        open(dst, "w").write(derive_solutions(txt))
        print(f"wrote {dst}")
        sys.exit(0)
    src, dst = args[0], args[1]
    txt = open(src).read()
    problems = check_markers(txt, src)
    if problems:
        for p in problems:
            print(p, file=sys.stderr)
        sys.exit(1)
    out = derive(txt)
    open(dst, "w").write(out)
    n_ans = len(BLANK.findall(out))
    n_off = len(re.findall(r"^#\| eval: false$", out, flags=re.M))
    n_left = len(re.findall(r"\.answer|Reveal (answer|solution)", out))
    print(f"wrote {dst}: {n_ans} blanks; {n_off} chunks with eval: false; {n_left} answer markers left")

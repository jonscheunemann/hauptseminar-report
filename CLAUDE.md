# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is a Hauptseminar (graduate seminar) deliverable for a course on altermagnetism at the
University of Stuttgart. It contains two related but independently-built artifacts:

- **`main.tex`** — the written report (LaTeX), "Altermagnets and spin liquids" by Jonas
  Scheunemann, supervised by Prof. Mathias Scheurer and MSc. Bernhard Putzer. This is the
  handout/written companion to the talk in `presentation/`.
- **`presentation/`** — the slide deck actually given ("Altermagnets and Spin Liquids.odp"/`.pptx`)
  plus a small Python script to dump the deck's text/speaker notes to a `.txt` file.

There is no code relationship between the two (no shared build, no imports across them).

## Report scope and source material

The report's content is governed by `goal/presentation_goal.txt`, which states the mandate:
introduce spin liquids and parton theory (spin fractionalization into bosons/fermions under
constraints), then discuss what spin-liquid phases emerge near a square-lattice altermagnet,
based on the paper in `papers/`.

Two source PDFs live in `papers/`, and **only specific chapters of each are in scope** — do not
pull content from the rest of these papers when writing or checking the report:

- `papers/PhysRevResearch.7.023152.pdf` (Sobral, Mandal, Scheurer, *"Fractionalized altermagnets:
  From neighboring and altermagnetic spin liquids to spin-symmetric band splitting"*, Phys. Rev.
  Research 7, 023152) — this is the primary paper the talk and report are built on. In scope:
  **Sec. I (Introduction), Sec. II (Classical Phase Diagram), Sec. III (Nearby Spin Liquids)**.
  Sec. IV (Fractionalized Itinerant Systems) and Sec. V (Conclusion) are **out of scope**.
- `papers/Savary_2017_Rep._Prog._Phys._80_016502.pdf` (Savary & Balents, *"Quantum spin
  liquids: a review"*, Rep. Prog. Phys. 80, 016502) — background/theory reference. In scope:
  **Sec. 1 (Introduction) and Sec. 3 (Gauge theory)** only.

The slide deck's content and ordering were discussed and approved with the supervisor (Prof.
Scheurer), so **the report should follow the same structure and order as the presentation**, not
invent its own. The approved slide order (from `presentation/Altermagnets and Spin Liquids.txt`)
is: Introduction → The Model (checkerboard Heisenberg model, C4z-related sublattices) → Classical
Phase Diagram (incl. the spin-rotation-invariant observables: NN scalar products / nematic order,
and scalar spin chirality) → From Schwinger Bosons to Spin Liquids → Invariant Gauge Group (U(1)
vs. Z2) → Matching phases to Schwinger-boson Ansätze → Phase Diagram Overview → The Altermagnetic
Spin Liquid → Summary of the classical magnetic phases → Neighbors and their SR observables →
(orbital altermagnet / scalar spin chirality ↔ orbital currents) → Experimental Outlook.

`presentation/spin-liquids-notes.txt` and `presentation/Altermagnets and Spin Liquids.txt` are two
extractions of the same deck (raw speaker notes vs. per-slide text); they are the primary prose
source to draw on when drafting report sections, since they contain the actual explanations used
in the talk. Note: `main.tex`'s current abstract and section placeholders were drafted before this
scope was finalized and have not yet been reconciled with it — check `goal/presentation_goal.txt`
and the slide order above before trusting existing body text as authoritative.

## Report (LaTeX)

Build with a standard `pdflatex` + `biber` cycle (bibliography uses `biblatex`/`biber`, not
`bibtex`):

```bash
pdflatex main.tex && biber main && pdflatex main.tex && pdflatex main.tex
```

Two `pdflatex` passes after `biber` are needed to resolve cross-references and the bibliography.

Structure of `main.tex`:
- A manually-built title block (title/author/affiliation/seminar/supervisors/date defined as
  `\newcommand`s near the top, rendered inside a `\begin{center}` block) — there is **no**
  `\maketitle`/`\title`/`\author`, so edit the `\reporttitle`, `\reportauthor`,
  `\reportaffiliation`, `\reportseminar`, `\reportsupervisors`, `\reportdate` commands directly
  rather than looking for standard LaTeX title macros.
- Abstract is inline (`\begin{center}{\bfseries Abstract}\end{center}` + a paragraph), not the
  `abstract` environment, and stays on page 1 under the title block rather than on a separate
  title page.
- Bibliography entries go in `references.bib`; `\printbibliography` renders them at the end.
- Figures belong in `figures/` (currently empty).

LaTeX build artifacts (`main.aux`, `.bbl`, `.bcf`, `.blg`, `.fdb_latexmk`, `.fls`, `.log`, `.out`,
`.run.xml`, `.synctex.gz`, `main.pdf`) are currently untracked/uncommitted cruft sitting in the
repo root — there is no `.gitignore` yet, so be careful not to `git add` these when committing.

## Presentation text extraction (Python)

Python dependencies are managed with `uv` (`pyproject.toml` + `uv.lock`, Python >=3.12 pinned via
`.python-version`). Install/sync with:

```bash
uv sync
```

`presentation/extract_notes.py` is a one-off script, run from inside `presentation/`:

```bash
cd presentation && uv run python extract_notes.py
```

It auto-discovers the first `*.odp` file in the current directory (does not take a filename
argument), extracts per-slide text/notes via `pptx2txt2`, and writes wrapped output to
`spin-liquids-notes.txt` — a hardcoded output filename. The script also dumps the first 20000
characters of the ODP's raw `content.xml` to stdout for debugging.

The repo root `main.py`/`pyproject.toml` `uv` project is scaffolding from `uv init` and is not
actually used by the report or the extraction script's logic.

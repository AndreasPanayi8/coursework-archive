# Coursework & Research Archive

A curated archive of coursework, presentations, lecture notes, code, and research material collected across my studies in mathematics and theoretical computer science at the National Technical University of Athens (NTUA) and the National & Kapodistrian University of Athens (NKUA).

The repository doubles as my [personal webpage](https://andreaspanayi8.github.io/coursework-archive/), served from GitHub Pages. Alongside sections on education, research, publications, engineering projects, and skills, the site embeds *The Library* — a browsable view of this archive with search, a folder tree, and inline previews of PDFs, notebooks, code, and slides.

## Contents

- **Archimedes Research Unit** — reports and code from my internship at the Archimedes Research Unit, Athena Research Center: an advanced data structures report, a computational geometry report, and C++ and Python implementations of Sundar's priority queue with attrition (PQA), in amortized and worst-case variants.
- **Exercises and Labs by Course** — problem sets, solved exercises, lab work, and reference books organized by course:
  - Advanced AI
  - Algorithmic Data Science
  - Algorithms
  - Approximation Algorithms
  - Blockchain Foundations
  - Combinatorial Optimization
  - Computational Complexity
  - Graph Theory
  - Machine Learning (including Python notebooks and lab code)
  - Network Algorithms and Complexity
  - Parametrized Complexity and Algorithms
  - Randomized Algorithms
  - Recursion Theory
  - Structural Complexity
- **Presentations** — slide decks from seminar and course talks, each paired with the papers and notes they are based on: communication complexity, exact edge-cover in temporal graphs, Goldberg–Rao max-flow, lossy kernelization, smoothed analysis, CSP inapproximability (Raghavendra), Cook's theorem, and halting/recursion theory.
- **LaTeX Intro and Template** — a short introduction to (Xe)LaTeX plus reusable `.tex` templates and preambles.
- **Thesis** — my MSc thesis, *Faster Even-Cycle Listing via Unbalanced Supersaturation*, together with the defense presentation.
- **CV** — academic and technical versions of my curriculum vitae.

## Publications

- *Listing Even Cycles Faster than the Submodular-Width Barrier* — Vasileios Nakos, Hung Q. Ngo, Andreas Panayi. [arXiv preprint](https://arxiv.org/abs/2605.30564), submitted to SIGMOD/PODS.
- *Faster Even-Cycle Listing via Unbalanced Supersaturation* — MSc thesis, NKUA. [Pergamos record](https://pergamos.lib.uoa.gr/en/item/uoadl:5402752).

## How the site is built

The site is a single static page with no build step or dependencies:

- `index.html` — the entire page: markup, styles, and scripts inline.
- `manifest.json` — a JSON tree of every directory and file in the archive; the file browser reads it at load time.
- `gen_manifest.py` — regenerates `manifest.json` by walking the repository, skipping dotfiles, OS junk, and editor folders.

After adding, renaming, or removing files in the archive, regenerate the manifest so the browser picks up the change:

```bash
python3 gen_manifest.py
```

Then commit both the new content and the updated `manifest.json`.

## About

I'm a theoretical computer science graduate student working on fine-grained and parameterized algorithms, dynamic and geometric data structures, and extremal graph theory, with applied interests in data management, big data, and machine learning.

- Webpage: https://andreaspanayi8.github.io/coursework-archive/
- Google Scholar: https://scholar.google.com/citations?user=ZMQ-fdQAAAAJ&hl=en&oi=ao
- ORCID: https://orcid.org/0009-0007-2703-5130
- GitHub: https://github.com/andreaspanayi8
- LinkedIn: https://www.linkedin.com/in/antreas-panagi/

## License

Unless otherwise stated, written materials in this repository are licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Code files are licensed under the [MIT License](https://opensource.org/licenses/MIT).

Third-party books, papers, lecture notes, slides, and reference materials remain under their original licenses and copyrights, and are included here for study and reference only.

# Papers

A scaffold for writing and publishing academic papers using **Markdown** as the
source format, **Pandoc** for conversion to LaTeX/PDF, and **GitHub Pages** for
automatic online publication.

---

## Repository Layout

```
papers/
├── papers/                   # One sub-directory per paper
│   └── example/
│       └── example.md        # Markdown source of the paper
├── templates/
│   └── paper.tex             # Pandoc LaTeX template
├── Makefile                  # Local build helper
└── .github/workflows/
    └── build-and-publish.yml # CI: build PDFs → deploy to GitHub Pages
```

---

## Writing a New Paper

1. Create a directory inside `papers/` named after your paper:
   ```bash
   mkdir papers/my-paper
   ```
2. Create a Markdown file with the same name:
   ```bash
   cp papers/example/example.md papers/my-paper/my-paper.md
   ```
3. Edit the YAML front matter at the top of the file.
4. Write your paper in Markdown below the front matter.

### Front Matter Reference

```yaml
title: "Full Paper Title"
runningtitle: "Short Title for Header"
runningauthor: "Smith et al."
authors:
  - fnms: "First"          # First / middle name(s)
    snm: "Author"          # Surname
    label: "A"             # Affiliation label
    orcid: "0000-0000-0000-0000"   # optional
    corresponding: true    # optional – adds corresponding-author note
    note: "contact@example.org"    # optional – contact info for corresponding author
  - fnms: "Second"
    snm: "Author"
    label: "B"
addresses:
  - label: "A"
    institution: "Department of CS, University of X, City, Country"
  - label: "B"
    institution: "Institute of Y, City, Country"
abstract: |
  Your abstract text here.
keywords:
  - keyword one
  - keyword two
booktitle: "Title of the Book"     # optional
bookeditors: "B. Editor et al."    # optional
bibliography: references.bib       # optional – relative to the paper directory
```

---

## Building Locally

You need **Pandoc** and a **LaTeX** distribution (e.g. TeX Live or MiKTeX)
installed on your machine.

```bash
# Build all papers as PDFs (output goes to build/)
make

# Build only LaTeX (.tex) files
make texs

# Clean generated files
make clean

# Show all available targets
make help
```

---

## Automatic Publishing (CI/CD)

Every push to `main` that touches a `papers/**/*.md` file, a template, or the
`Makefile` triggers the **Build and Publish Papers** GitHub Actions workflow
(`.github/workflows/build-and-publish.yml`). The workflow:

1. Installs Pandoc and TeX Live on the runner.
2. Runs `make all` to build every paper to PDF.
3. Generates an `index.html` with download links to all PDFs.
4. Deploys the `build/` directory to **GitHub Pages**.

> **Enable GitHub Pages**: go to *Settings → Pages* in your repository and set
> the source to **GitHub Actions**.

Once deployed, your papers are available at:
`https://<your-github-username>.github.io/papers/`

---

## LaTeX Template

The template lives in `templates/paper.tex` and targets the **IOS Press Book
Article** format using the `IOS-Book-Article.cls` class file
(from [vtex-soft/texsupport.IOS-Book-Article](https://github.com/vtex-soft/texsupport.IOS-Book-Article)).
The class file (`IOS-Book-Article.cls`) and Vancouver bibliography style
(`vancouver.bst`) are included in `templates/` and are automatically copied to
the build directory at compile time.

The template supports:

- Title, running title, running author
- Multiple authors with `\fnms{}` / `\snm{}`, ORCID, affiliations, corresponding-author footnote
- Abstract and keywords (`\sep`-delimited)
- Book title and editors (for book chapter attribution)
- Mathematics (`amsmath`, `amssymb`)
- Code listings with syntax highlighting
- Tables (`booktabs`, `longtable`)
- BibTeX bibliography via `vancouver.bst` (add `bibliography: references.bib` to front matter)

Feel free to modify the template to match your target journal or conference
style.

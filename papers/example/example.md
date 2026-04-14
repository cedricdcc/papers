---
title: "Example Paper"
author: "Author Name"
date: "2026-04-14"
abstract: |
  This is an example paper demonstrating how to write papers using Markdown
  in this repository. The paper will be automatically converted to LaTeX and
  compiled to a PDF when changes are pushed to the main branch.
keywords: [example, markdown, latex, pandoc]
---

# Introduction

This is the introduction section of your paper. Write your content here using
standard Markdown syntax. All standard Markdown features are supported,
including **bold text**, *italic text*, `inline code`, and more.

# Background

You can include mathematical equations using LaTeX syntax. For example, inline
math like $E = mc^2$, or display equations:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

# Methodology

## Subsections

Subsections work with standard Markdown headings.

## Code Blocks

Code blocks are also supported:

```python
def hello_world():
    print("Hello, World!")
```

# Results

You can include tables:

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
| Value 4  | Value 5  | Value 6  |

# Discussion

Discuss your findings here.

# Conclusion

Conclude your paper here.

# References

Include your references here. You can also use a `.bib` file for BibTeX
references by adding `bibliography: references.bib` to the front matter and
citing with `[@key]`.

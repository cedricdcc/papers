## Variables (override on the command line if needed)
TEMPLATE      := templates/paper.tex
IOS_CLS       := templates/IOS-Book-Article.cls
VANCOUVER_BST := templates/vancouver.bst
PAPERS_DIR    := papers
BUILD_DIR     := build

## Find all papers: papers/<name>/<name>.md  (only the file matching the directory name)
PAPER_DIRS := $(wildcard $(PAPERS_DIR)/*/)
SOURCES    := $(foreach dir,$(PAPER_DIRS),$(wildcard $(dir)$(notdir $(patsubst %/,%,$(dir))).md))
PDFS    := $(patsubst $(PAPERS_DIR)/%.md,$(BUILD_DIR)/%.pdf,$(SOURCES))
TEXS    := $(patsubst $(PAPERS_DIR)/%.md,$(BUILD_DIR)/%.tex,$(SOURCES))

.PHONY: all pdfs texs clean help

## Default target: build all PDFs
all: pdfs

## Build all PDFs
pdfs: $(PDFS)

## Build all LaTeX (.tex) files only
texs: $(TEXS)

## Shared helper: copy IOS style files into a build sub-directory
define copy-ios-files
	@mkdir -p $(dir $@)
	cp $(IOS_CLS) $(dir $@)
	cp $(VANCOUVER_BST) $(dir $@)
endef

## Convert a Markdown paper to LaTeX
$(BUILD_DIR)/%.tex: $(PAPERS_DIR)/%.md $(TEMPLATE) $(IOS_CLS) $(VANCOUVER_BST) | $(BUILD_DIR)
	$(copy-ios-files)
	pandoc "$<" \
	  --template=$(TEMPLATE) \
	  --standalone \
	  --citeproc \
	  --from=markdown+link_attributes \
	  --to=latex \
	  --resource-path=$(dir $<) \
	  -o "$@"
	@echo "Generated LaTeX: $@"

## Convert a Markdown paper to PDF (via LaTeX)
$(BUILD_DIR)/%.pdf: $(PAPERS_DIR)/%.md $(TEMPLATE) $(IOS_CLS) $(VANCOUVER_BST) | $(BUILD_DIR)
	$(copy-ios-files)
	pandoc "$<" \
	  --template=$(TEMPLATE) \
	  --standalone \
	  --citeproc \
	  --from=markdown+link_attributes \
	  --pdf-engine=lualatex \
	  --pdf-engine-opt=-output-directory=$(dir $@) \
	  --resource-path=$(dir $<) \
	  -o "$@"
	@echo "Generated PDF: $@"

PYTHON         ?= $(shell which python3 2>/dev/null || which python 2>/dev/null || echo python)

## Posters
POSTERS_DIR    := posters
POSTER_DIRS    := $(wildcard $(POSTERS_DIR)/*/)
POSTER_SOURCES := $(foreach dir,$(POSTER_DIRS),$(wildcard $(dir)poster.tex))
POSTER_PDFS    := $(patsubst $(POSTERS_DIR)/%/poster.tex,$(BUILD_DIR)/posters/%.pdf,$(POSTER_SOURCES))

.PHONY: all pdfs texs posters audit-pptx clean help

## Build all LaTeX poster PDFs
posters: $(POSTER_PDFS)

$(BUILD_DIR)/posters/%.pdf: $(POSTERS_DIR)/%/poster.tex | $(BUILD_DIR)
	@mkdir -p "$(dir $@)"
	pdflatex -jobname="$*" -interaction=nonstopmode -output-directory="$(dir $@)" "$<"
	@echo "Generated Poster PDF: $@"

## Audit an existing PPTX poster (Usage: make audit-pptx file=path/to/poster.pptx)
audit-pptx:
	$(PYTHON) posters/pptx-workflow/audit_existing_pptx.py $(file)

## Audit poster against Mixed-Approach Rubric (Usage: make audit-rubric file=path/to/poster)
audit-rubric:
	$(PYTHON) .agents/skills/poster-design-strategy/scripts/audit_poster_rubric.py $(file)

## Create the build directory
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

## Remove all generated files
clean:
	rm -rf $(BUILD_DIR)

## Show help
help:
	@echo "Usage:"
	@echo "  make              - Build all papers as PDFs (default)"
	@echo "  make pdfs         - Build all papers as PDFs"
	@echo "  make texs         - Build all papers as LaTeX (.tex) files"
	@echo "  make posters      - Build all LaTeX posters in posters/*/"
	@echo "  make audit-pptx file=<poster.pptx> - Audit existing PPTX poster layout"
	@echo "  make clean        - Remove all generated files"
	@echo ""
	@echo "To add a new paper:"
	@echo "  1. Create a directory:  papers/<paper-name>/"
	@echo "  2. Add a Markdown file: papers/<paper-name>/<paper-name>.md"
	@echo "  3. Run 'make' to build"
	@echo ""
	@echo "To add a new poster:"
	@echo "  1. Create a directory:  posters/<poster-name>/"
	@echo "  2. Add poster.tex (using templates/posters/*.tex)"
	@echo "  3. Run 'make posters' to build"

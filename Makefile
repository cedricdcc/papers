## Variables (override on the command line if needed)
TEMPLATE   := templates/paper.tex
PAPERS_DIR := papers
BUILD_DIR  := build

## Find all papers: papers/<name>/<name>.md
SOURCES := $(wildcard $(PAPERS_DIR)/*/*.md)
PDFS    := $(patsubst $(PAPERS_DIR)/%.md,$(BUILD_DIR)/%.pdf,$(SOURCES))
TEXS    := $(patsubst $(PAPERS_DIR)/%.md,$(BUILD_DIR)/%.tex,$(SOURCES))

.PHONY: all pdfs texs clean help

## Default target: build all PDFs
all: pdfs

## Build all PDFs
pdfs: $(PDFS)

## Build all LaTeX (.tex) files only
texs: $(TEXS)

## Convert a Markdown paper to LaTeX
$(BUILD_DIR)/%.tex: $(PAPERS_DIR)/%.md $(TEMPLATE) | $(BUILD_DIR)
	@mkdir -p $(dir $@)
	pandoc "$<" \
	  --template=$(TEMPLATE) \
	  --standalone \
	  --from=markdown \
	  --to=latex \
	  -o "$@"
	@echo "Generated LaTeX: $@"

## Convert a Markdown paper to PDF (via LaTeX)
$(BUILD_DIR)/%.pdf: $(PAPERS_DIR)/%.md $(TEMPLATE) | $(BUILD_DIR)
	@mkdir -p $(dir $@)
	pandoc "$<" \
	  --template=$(TEMPLATE) \
	  --standalone \
	  --from=markdown \
	  --pdf-engine=pdflatex \
	  -o "$@"
	@echo "Generated PDF: $@"

## Create the build directory
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

## Remove all generated files
clean:
	rm -rf $(BUILD_DIR)

## Show help
help:
	@echo "Usage:"
	@echo "  make          - Build all papers as PDFs (default)"
	@echo "  make pdfs     - Build all papers as PDFs"
	@echo "  make texs     - Build all papers as LaTeX (.tex) files"
	@echo "  make clean    - Remove all generated files"
	@echo ""
	@echo "To add a new paper:"
	@echo "  1. Create a directory:  papers/<paper-name>/"
	@echo "  2. Add a Markdown file: papers/<paper-name>/<paper-name>.md"
	@echo "  3. Run 'make' to build"

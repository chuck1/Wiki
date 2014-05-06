
MKDIR = mkdir -p

SOURCE_DIR = src
BINARY_DIR = build

MARKDOWN = perl ~/Documents/Programming/Markdown/Markdown_1.0.1/Markdown.pl --html4tags

MD_FILES = $(shell find $(SOURCE_DIR) -name *.md)
DOT_FILES = $(shell find $(SOURCE_DIR) -name *.dot)

DOT_PNG_FILES = $(patsubst $(SOURCE_DIR)%.dot, $(BINARY_DIR)%.png, $(DOT_FILES))

SRC_PNG_FILES = $(shell find $(SOURCE_DIR) -name *.png)
BIN_PNG_FILES = $(patsubst $(SOURCE_DIR)%.png, $(BINARY_DIR)%.png, $(SRC_PNG_FILES))

HTML_FILES = $(patsubst $(SOURCE_DIR)%.md, $(BINARY_DIR)%.html, $(MD_FILES))


all: $(HTML_FILES) $(DOT_PNG_FILES) $(BIN_PNG_FILES)

HEADER1 = "<head><link href=\"http://kevinburke.bitbucket.org/markdowncss/markdown.css\" rel=\"stylesheet\"></link>"
HEADER2 = "<script type=\"text/javascript\"src=\"http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\"></script></head>"

$(BIN_PNG_FILES): $(BINARY_DIR)%.png: $(SOURCE_DIR)%.png
	@$(MKDIR) $(dir $@)
	@cp $< $@

$(DOT_PNG_FILES): $(BINARY_DIR)%.png: $(SOURCE_DIR)%.dot
	@$(MKDIR) $(dir $@)
	@dot -tpng $< > $@
	
$(HTML_FILES): $(SOURCE_DIR)%.html: $(BINARY_DIR)%.md
	@$(MKDIR) $(dir $@)
	@echo $(HEADER1) > $@
	@echo $(HEADER2) >> $@
	$(MARKDOWN) $< >> $@



test:
	@echo $(MD_FILES)
	@echo $(DOT_FILES)
	@echo $(HTML_FILES)
	@echo $(DOT_PNG_FILES)

clean:
	rm -rf build




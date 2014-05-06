
SOURCE_DIR = src
BINARY_DIR = build

MARKDOWN = perl ~/Documents/Programming/Markdown/Markdown_1.0.1/Markdown.pl --html4tags

G_FILES = $(shell find $(SOURCE_DIR) -name *.mdg)

MD_FILES = $(patsubst $(SOURCE_DIR)%.mdg, $(BINARY_DIR)%.md, $(G_FILES))

HTML_FILES = $(patsubst $(BINARY_DIR)%.md, $(BINARY_DIR)%.html, $(MD_FILES))



all: $(HTML_FILES)

HEADER1 = "<head><link href=\"http://kevinburke.bitbucket.org/markdowncss/markdown.css\" rel=\"stylesheet\"></link>"
HEADER2 = "<script type=\"text/javascript\"src=\"http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\"></script></head>"



$(MD_FILES): $(BINARY_DIR)%.md: $(SOURCE_DIR)%.mdg
	@mkdir -p $(dir $@)
	python graphviz.py $< $@

$(HTML_FILES): $(BINARY_DIR)%.html: $(BINARY_DIR)%.md
	@echo $(HEADER1) > $@
	@echo $(HEADER2) >> $@
	$(MARKDOWN) $< >> $@
	

test:
	@echo $(G_FILES)
	@echo $(MD_FILES)
	@echo $(HTML_FILES)

clean:
	rm -rf build/*




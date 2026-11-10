# Perl Taster build. Paperback interior follows Perl School FORMATTING.md
# (perlschool-util), at 6" x 9" trim.
#
# Needs: pandoc, XeLaTeX (with fvextra, titlesec, tocloft, imakeidx, emptypage,
# footmisc, xurl), makeindex, and the fonts EB Garamond, Montserrat and
# DejaVu Sans Mono installed.

BOOK  = perl-taster
BUILD = build
GEOM  = paperwidth=6in,paperheight=9in,inner=24mm,outer=18mm,top=20mm,bottom=22mm,headsep=6mm,footskip=11mm
XELATEX = cd $(BUILD) && TEXINPUTS=..: xelatex -interaction=nonstopmode -halt-on-error $(BOOK)-kdp.tex >/dev/null

.PHONY: all epub kdp cover guides clean

all: epub kdp

epub: $(BOOK).epub

$(BOOK).epub: $(BOOK).md epub.css cover.jpg
	pandoc $(BOOK).md -f markdown+smart -o $@ --css epub.css --toc --toc-depth=2

kdp: $(BOOK)-kdp.pdf

$(BOOK)-kdp.pdf: $(BOOK).md print/*
	mkdir -p $(BUILD)
	pandoc $(BOOK).md -f markdown-raw_tex+smart -L print/print-links.lua \
	  -s -o $(BUILD)/$(BOOK)-kdp.tex \
	  -V documentclass=book -V classoption=openright -V fontsize=11pt \
	  -V geometry:"$(GEOM)" -V lang=en-GB \
	  -V pagetitle="Perl Taster" -V author-meta="Dave Cross" \
	  -M title= -M subtitle= -M author= \
	  -H print/head.tex -B print/front.tex -A print/back.tex \
	  --top-level-division=chapter --number-sections --no-highlight
	$(XELATEX)
	$(XELATEX)
	cd $(BUILD) && makeindex -q $(BOOK)-kdp.idx
	$(XELATEX)
	$(XELATEX)
	cp $(BUILD)/$(BOOK)-kdp.pdf $@

clean:
	rm -rf $(BUILD) $(BOOK).epub $(BOOK)-kdp.pdf $(BOOK)-cover.pdf $(BOOK)-cover.png

# One-piece paperback cover (front, spine, back) for KDP. PAGES must match
# the interior page count that KDP reports (it rounds odd counts up).
PAGES = 54
cover: $(BOOK)-cover.pdf

$(BOOK)-cover.pdf: cover/make_cover.py cover.jpg pearl-2045162_1920.jpg
	python3 cover/make_cover.py $(PAGES) $(BOOK)-cover

guides: cover/make_cover.py
	python3 cover/make_cover.py $(PAGES) $(BUILD)/cover-guides --guides

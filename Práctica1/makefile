all: $(file) clean

$(file): $(file).tex
	pdflatex --shell-escape $(file).tex
	pdflatex --shell-escape $(file).tex

clean:
	rm *.bbl *.aux *.blg *.fdb_latexmk *.out *.log *.toc *.fls *.lof *.lot

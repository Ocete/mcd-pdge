file=P2 # Valor por defecto

all: clean $(file) clean

$(file): clean
	pdflatex --shell-escape $(file).tex
	pdflatex --shell-escape $(file).tex

clean:
	rm -f *.bbl *.aux *.blg *.fdb_latexmk *.out *.log *.toc *.fls *.lof *.lot
	rm -rf _minted-*

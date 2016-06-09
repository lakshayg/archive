echo "\documentclass{article}" >> "merged.tex"
echo "\usepackage{pdfpages}" >> "merged.tex"
echo "\begin{document}" >> "merged.tex"
for f in *.pdf; do
  echo "\includepdf[pages=-,fitpaper=true]{$f}" >> "merged.tex"; 
done
echo "\end{document}" >> "merged.tex"
pdflatex "merged.tex"
rm -rf *.aux *.log *.tex
echo "Done"

set title 'Temps pour itérer sur une liste'
set term png
set output 'time.png'
set ylabel "temps"
set xlabel 'longueur de la liste'
plot 'time.tsv' using 1:2 title 'get' w l lw 4, \
  '' using 1:3 title 'itérateur' w l lw 4
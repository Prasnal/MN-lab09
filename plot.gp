set term png
set out 'rysunek.png'
set xlabel "x"
set ylabel "y" rotate parallel
plot 'zad1.dat' u 1:2 w l,'zad1.dat' u 1:3 w l

set term png
set out 'rysunek2.png'
set xlabel "x"
set ylabel "y" rotate parallel
plot 'zad2.dat' u 1:2 w l,'zad2.dat' u 1:3 w l

set term png
set out 'rysunek3.png'
set xlabel "x"
set ylabel "y" rotate parallel
plot 'zad3.dat' u 1:2 w l,'zad3.dat' u 1:3 w l,'zad3.dat' u 1:4 w l,'zad3.dat' u 1:5 w l,'zad3.dat' u 1:6 w l


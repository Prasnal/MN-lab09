all:
	@rm -f *.dat
	@rm -f *.png
	@python main.py
	@gnuplot plot.gp


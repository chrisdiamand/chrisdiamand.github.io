all: assets/css/main.css

assets/css/main.css: assets/sass/main.scss Makefile cssmap2depfile.py
	sassc --style expanded -mauto $< $@
	./cssmap2depfile.py $@.map assets/css/main.css.d
	touch $@

-include assets/css/main.css.d

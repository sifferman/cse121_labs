
AUTOGRADERS := build/autograder_lab1.zip \
               build/autograder_lab2.zip \
               build/autograder_lab3.zip \
               build/autograder_lab4.zip \
               build/autograder_lab5.zip \
               build/autograder_lab6.zip

all: clean ${AUTOGRADERS}

build/autograder_%.zip:
	rm -rf $@ build/$*
	mkdir -p build
	cp -r autograder/ build/$*/
	cat autograder/generate_results/run_tests/test_all.py.1 $*.py.2 > build/$*/generate_results/run_tests/test_all.py
	cd build/$* && zip -r ../autograder_$*.zip *

clean:
	rm -rf build

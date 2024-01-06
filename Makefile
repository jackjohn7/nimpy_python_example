##
# Nimpy Web Example
#
# @file
# @version 0.1

build_nim_lib:
	echo "Building nim library"
	nim c --app:lib --out:nimpy_web_example.so --threads:on src/nimpy_web_example

install_py_deps:
	pip install -r requirements.txt

run:
	make build_nim_lib
	echo "Executing main.py"
	python3 main.py

# end


mkenv:
	pyvenv-3.4 .virtualenv

install:
	test -d .virtualenv || ${MAKE} mkenv
	. .virtualenv/bin/activate; pip install -r requirements

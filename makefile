mkenv:
	pyvenv-3.4 .virtualenv

install:
	test -d .virtualenv || ${MAKE} mkenv
	. .virtualenv/bin/activate; pip install -r requirements
	npm install

test:
	. .virtualenv/bin/activate; cd src && python manage.py test --keepdb

travis-install:
	pip install -r requirements

travis-test:
	cd src && python manage.py test --keepdb

#!make
# include .env
# SHELL := /bin/bash
# export $(shell sed 's/=.*//' .env)


# NOTE: create a file called .env (clone .env.sample)
# and fill in your keys

gen-docs:
	mdbook build

django-dev:
	@echo "Django Version:" $(shell python -m django --version)
	python manage.py runserver 8070

django-migrate:
	python manage.py makemigrations
	python manage.py migrate

django-format:
	python -m black .

django-createsuperuser:
	#@REM creds are admin:password
	python manage.py createsuperuser

python-freeze:
	python -m pip freeze > requirements.txt

copy-react:
	cd autogrant && npm run build
	mv ./autogrant/dist/assets/index*.js ./website/static/dist/js/react.js
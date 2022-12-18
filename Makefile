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

copy-vite:
	cd autogrant && npm run build
	cp ./autogrant/dist/assets/index*.js ./website/static/dist/js/react.js

copy-esbuild: # for debug js file
	./autogrant/node_modules/.bin/esbuild ./autogrant/src/main.jsx --bundle --sourcemap --outfile=/home/icewreck/Development/capstone/website/static/dist/js/react.js

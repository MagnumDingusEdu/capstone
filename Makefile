#!make
include .env
SHELL := /bin/bash
export $(shell sed 's/=.*//' .env)


# NOTE: create a file called .env (clone .env.sample)
# and fill in your keys

gen-docs:
	mdbook build
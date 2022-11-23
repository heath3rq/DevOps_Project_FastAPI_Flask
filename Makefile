install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		curl -sSL https://get.docker.com/ | sudo sh
		sudo apt-get update && sudo apt-get upgrade

test:
	python -m pytest -vv test_*.py

format:	
	black *.py

lint:
	pylint --disable=R,C test_hello.py

build:
	docker build -t deploy-fastapi .

all: install lint test format build
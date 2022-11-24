install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		python -m pip install "dask[dataframe]" --upgrade
		curl -sSL https://get.docker.com/ | sudo sh

test:
	python -m pytest -vv --cov=app test_*.py

format:	
	black *.py

lint:
	pylint --disable=R,C,W1203,W0702 *.py

# build:
# 	docker build -t deploy-fastapi .

all: install lint test format
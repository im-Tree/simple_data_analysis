install:
	pip install -r requirements.txt

format:
	black *.py
	
lint:
	flake8 --ignore=E501,N8,C,W503,W291 *.py

test:
	pytest

run:
	python gold_price_analysis.py

clean:
	rm -rf __pycache__ *.pyc
	rm -rf .pytest_cache	

all: install format lint test	
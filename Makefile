format:
	python -m black --line-length 79 .

lint:
	flake8 .

test:
	pytest -v -s

build:
	python3 -m build
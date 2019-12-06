.PHONY: activate req freeze format

activate:
	sh .venv/bin/activate

req:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

format: activate req
	black .

test:	#activate req
	python -m unittest discover tests

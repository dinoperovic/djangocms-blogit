clean:
	rm -rf dist/ build/ *.egg-info .coverage .DS_Store
	find . -name '*.pyc' -exec rm '{}' ';'

lint:
	flake8 --exclude=.git,migrations,docs --max-complexity=10 .

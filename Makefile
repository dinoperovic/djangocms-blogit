clean:
	rm -rf dist/ build/ .tox/ *.egg-info .coverage .DS_Store
	find . -name '*.pyc' -exec rm '{}' ';'

lint:
	flake8 --exclude=.git,migrations,docs,.tox --max-complexity=10 .

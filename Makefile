clean:
	rm -rf dist/ build/ *.egg-info .coverage .DS_Store
	find . -name '*.pyc' -exec rm '{}' ';'

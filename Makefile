clean:
	rm -rf dist/ build/ *.egg-info
	find . -name '*.pyc' -exec rm '{}' ';'

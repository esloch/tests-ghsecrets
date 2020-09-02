install:
	pip install -e .

configure_environ:
	bash .github/workflows/scripts/update_credentials_environ.sh
	python config.py

list_dir:
	python upload_.py

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

print_key:
	python print_secrets.py

SRC=snap.py

help: ## Show this help information
	$(info Available commands:)
	@grep '^[[:alnum:]_-]*:.* ##' $(MAKEFILE_LIST) \
	 | sort | awk 'BEGIN {FS=":.* ## "}; {printf "%-25s %s\n", $$1, $$2};'

flake8: ## Check Python source for PEP8 style guidance
	$(info Running: flake8 --max-complexity 10 $(SRC))
	@if type flake8 >/dev/null 2>&1 ; then flake8 --max-complexity 10 $(SRC) ; \
	 else echo 'SKIPPED. Please run `pip install -r requirements.txt`!' >&2; fi

mypy: ## Check Python source for type errors
	$(info Running: mypy --ignore-missing-imports $(SRC))
	@if type mypy >/dev/null 2>&1; then mypy --ignore-missing-imports $(SRC); \
	 else echo 'SKIPPED. Please run `pip install -r requirements.txt`!' >&2; fi

lint: flake8 mypy ## Run linting tools

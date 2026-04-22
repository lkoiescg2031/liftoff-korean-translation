PYTHON ?= python3
SCRIPT ?= compare_translation_keys.py
BASE_CSV ?= TranslationSpreadsheet.csv
KO_CSV ?= TranslationSpreadsheet.ko.csv
LOG_FILE ?= compare_result.log

.PHONY: compare

compare:
	$(PYTHON) $(SCRIPT) $(BASE_CSV) $(KO_CSV) | tee $(LOG_FILE)

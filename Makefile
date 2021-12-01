.PHONY: test data data_d data_dr data_drn reset

test:
	pytest -xv --pylint --flake8 ./tests/test.py

data:
	python3 env_data/env_data.py new_data/*

data_d:
	python3 env_data/env_data.py new_data/* -d

data_dr:
	python3 env_data/env_data.py new_data/* -dr

data_drn:
	python3 env_data/env_data.py new_data/* -drn

reset:
	python3 reset/reset.py

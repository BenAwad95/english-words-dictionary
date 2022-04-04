include .env

start: $(PYTHON) $(APP_DIR)/manage.py runserver
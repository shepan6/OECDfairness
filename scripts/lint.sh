isort ethically tests
black ethically tests
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
pycodestyle --show-source --show-pep8 ethically tests
pycodestyle --statistics ethically tests
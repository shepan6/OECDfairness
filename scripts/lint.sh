isort src tests
black --line-length=78 src tests
flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 tests --count --select=E9,F63,F7,F82 --show-source --statistics
pycodestyle --statistics src tests
FROM python:3.11 as base
COPY README.md .
COPY setup.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src /src
RUN python setup.py bdist_wheel sdist

FROM base as dev
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt
COPY scripts /scripts
RUN pip install -e .

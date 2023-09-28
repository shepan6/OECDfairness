FROM python:latest as base
COPY setup.py .
COPY requirements.txt .
COPY src /src
RUN python setup.py bdist_wheel sdist
RUN pip install -e .
# RUN pip install -r requirements.txt

FROM base as dev
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt
COPY scripts /scripts

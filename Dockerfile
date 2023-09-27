FROM python:latest as base
COPY setup.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install .

FROM base as dev
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt
COPY scripts /app/scripts

FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

CMD streamlit run --server.port $PORT --server.address 0.0.0.0 main.py

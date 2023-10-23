FROM python:3.11

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR api
COPY . .

CMD uvicorn --host 0.0.0.0 sql_app.main:app --reload

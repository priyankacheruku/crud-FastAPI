FROM python:3.7

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 80

COPY ./ ./

CMD ["uvicorn", "book_store.main:app", "--host", "0.0.0.0", "--port", "80"]
FROM python:3

WORKDIR /usr/src/app

COPY . . 

RUN python -m venv .venv
RUN .\.ven\Scripts\activate
RUN pip install -r .\requeriments.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
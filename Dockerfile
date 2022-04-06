FROM python:alpine

COPY ./requirements.txt .


RUN pip install -r requirements.txt

COPY . .
ENV FLASK_APP=main.py
CMD ["python", "main.py"]


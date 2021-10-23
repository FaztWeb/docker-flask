FROM python:3.8.10

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["python", "src/app.py"]
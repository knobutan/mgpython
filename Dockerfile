FROM python:3.10.0a7-slim-buster
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080
CMD [ "python", "test.py" ] 

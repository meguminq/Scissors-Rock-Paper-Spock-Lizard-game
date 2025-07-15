FROM python:3.13.3

WORKDIR /app
COPY . .

CMD ["python", "rpslsgame.py"]
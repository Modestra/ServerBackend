FROM python:latest
WORKDIR /app
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

RUN ./backend .

WORKDIR /app/backend
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


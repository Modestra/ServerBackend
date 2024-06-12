FROM python:latest
WORKDIR /app
ENV PYTHONUNBUFFERED 1
EXPOSE 80

COPY ./backend .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary
RUN pip install -U drf-yasg

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


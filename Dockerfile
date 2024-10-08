FROM python:latest 
COPY . /usr/src/
WORKDIR /usr/src/backend
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install setuptools
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
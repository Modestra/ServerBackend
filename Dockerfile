FROM ubuntu:latest as github
RUN apt-get update
RUN apt-get install -y git
RUN git config --global user.email "umbrellamixmail@gmail.com"
RUN git config --global user.name "Modestra"
RUN git config --global user.password "Terrarik22"
RUN git clone "https://github.com/Modestra/ServerBackend.git"
RUN apt-get install python3 -y
RUN apt-get update
RUN apt-get install python3-pip -y --fix-missing

FROM python:latest 
COPY --from=github ServerBackend /usr/src/
WORKDIR /usr/src/backend
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
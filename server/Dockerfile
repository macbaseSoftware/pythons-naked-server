# set base image (host OS)
#FROM python:3.8

# set the working directory in the container
#WORKDIR /code

# copy the dependencies file to the working directory
#COPY requirements.txt .

# install dependencies
#RUN pip install -r requirements.txt


FROM ubuntu:16.04
RUN apt-get update -y
RUN apt-get install python -y
RUN apt-get install python-pip -y
RUN pip install flask
COPY requirements.txt /home/requirements.txt
COPY ./src /home/src
#COPY app.py /home/app.py
ENTRYPOINT FLASK_APP=/home/src/app.py flask run --host=0.0.0.0


# copy the content of the local src directory to the working directory
#COPY src/ .

# command to run on container start
#CMD [ "python ./app.py"] 

FROM python:3.9.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.pip /code/
RUN pip install -r requirements.pip
ADD . /code/
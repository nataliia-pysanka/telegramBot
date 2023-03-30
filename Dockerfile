# # pull official base image
# FROM python:3.9-alpine
#
# # set work directory
# WORKDIR /usr/src/src
#
# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
#
# # install dependencies
# RUN pip install --upgrade pip
# COPY ./requirements.txt /usr/src/src/requirements.txt
# RUN pip install -r requirements.txt
#
# # copy project
# COPY . /usr/src/src/
#
# EXPOSE 5000
#
# CMD [ "python3", "wsgi"]
# pull official base image
FROM python:3.8-alpine3.10

# set work directory
WORKDIR /code

# set environment variables
COPY requirements.txt /code/
# install dependencies
RUN set -ex \
    && apk add --no-cache postgresql-dev build-base cmake make mupdf-dev freetype-dev\
    && pip3 install --upgrade pip \
    && pip3 install -r requirements.txt
COPY . /code/	

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "regtur.wsgi:application"]
# copy project

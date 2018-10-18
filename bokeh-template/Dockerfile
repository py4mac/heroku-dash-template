#Grab the latest alpine image
FROM alpine:latest

# install dependencies
# the lapack package is only in the community repository
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --update add --no-cache \ 
    lapack-dev \ 
    gcc \
    freetype-dev

# Install python and pip
RUN apk add --no-cache --update python3 py3-pip bash

# Install dependencies
RUN apk add --no-cache --virtual .build-deps \
    gfortran \
    musl-dev \
    g++ \
    python3-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

ADD ./webapp/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install -r /tmp/requirements.txt

# Add our code
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp

# Expose is NOT supported by Heroku
# EXPOSE 5000 		

# Run the image as a non-root user
RUN adduser -D myuser
USER myuser

# removing dependencies
#RUN apk del .build-deps

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn --bind 0.0.0.0:$PORT wsgi 


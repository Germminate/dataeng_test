FROM python:3.7-alpine

USER root
ENV HOME /home

# Update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories

# Install chromedriver
RUN apk update
RUN apk add chromium \
    chromium-chromedriver \
    bash \
    vim

# Install requirements to run pip
RUN apk add --update make cmake gcc g++ gfortran
RUN apk add --update py3-pip

# Install required packages
RUN mkdir -p $HOME/solution
COPY ../solution/requirements.txt $HOME/solution/requirements.txt
RUN pip install -r  $HOME/solution/requirements.txt


# Copy entire solution directory
COPY ../solution/. $HOME/solution/.
WORKDIR $HOME/solution

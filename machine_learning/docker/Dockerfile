FROM python:3.9

USER root
ENV HOME /home

# Copy entire solution directory
RUN mkdir -p $HOME/solution
COPY ../solution/. $HOME/solution/.
WORKDIR $HOME/solution

FROM python:3.9.0b4-alpine3.12

USER root
ENV HOME /home

# Install packages (Installing packages fail when not run in docker)
COPY ../solution/requirements.txt $HOME/visualize/requirements.txt
RUN pip install -r $HOME/visualize/requirements.txt

# Copy directories for data processing
COPY ../solution $HOME/visualize/solution

WORKDIR $HOME/visualize/solution


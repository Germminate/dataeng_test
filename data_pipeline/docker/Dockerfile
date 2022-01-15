FROM python:3.9.0b4-alpine3.12

# Install vim for easy editing of scheduler
RUN apk update
RUN apk add bash \
    vim

# Install necessary packages
COPY ./solution/requirements.txt /bin/requirements.txt
RUN pip install -r /bin/requirements.txt

# Copy necessary files
COPY ./solution/scripts/data_prep /bin/data_prep
COPY ./solution/data /bin/data
COPY ./solution/scripts/root /var/spool/cron/crontabs/root
# Allow execution access
RUN chmod +x /bin/data_prep
# Start cron job with log level 1
CMD crond -l 1 -f
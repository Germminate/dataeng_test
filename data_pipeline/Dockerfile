FROM python:3.9.0b4-alpine3.12

# Install necessary packages
COPY requirements.txt /bin/requirements.txt
RUN pip install -r /bin/requirements.txt

# Copy necessary files
COPY data_prep /bin/data_prep
COPY data /bin/data
COPY root /var/spool/cron/crontabs/root
# Allow execution access
RUN chmod +x /bin/data_prep
# Start cron job with log level 1
CMD crond -l 1 -f
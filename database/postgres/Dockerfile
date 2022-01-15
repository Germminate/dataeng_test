# FROM postgres
FROM postgres:latest

# Setup Database
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password
ENV PGDATA=/var/lib/postgresql/data/pgdata
ENV POSTGRES_DB="Car_Dealership"

# Create database and generate data
COPY ./create_db.sql /docker-entrypoint-initdb.d/
COPY ./generate_data.sql /docker-entrypoint-initdb.d/

# Run queries
COPY ./queries/query1.sql /docker-entrypoint-initdb.d/
COPY ./queries/query2.sql /docker-entrypoint-initdb.d/

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# Expose the PostgreSQL port
EXPOSE 5432

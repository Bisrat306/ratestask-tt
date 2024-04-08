FROM  postgres:15
COPY rates.sql /docker-entrypoint-initdb.d/
EXPOSE 5432
ENV POSTGRES_PASSWORD=ratestask

CREATE DATABASE shivam;

CREATE USER shivam WITH PASSWORD 'shivam';
ALTER ROLE shivam SET client_encoding TO 'utf8';
ALTER ROLE shivam SET default_transaction_isolation TO 'read committed';
ALTER ROLE shivam SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE shivam TO shivam;
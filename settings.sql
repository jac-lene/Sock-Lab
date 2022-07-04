-- settings.sql
CREATE DATABASE socklab;
CREATE USER slabuser WITH PASSWORD 'slab';
GRANT ALL PRIVILEGES ON DATABASE socklab TO slabuser;
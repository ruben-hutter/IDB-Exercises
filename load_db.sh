#!/bin/bash

# Set the path to your SQL file
SQL_FILE=~/UNI/Introduction_to_DB/ex3.sql

# Set the Docker container name
CONTAINER_NAME=introdb-postgres

# Set the PostgreSQL username
PG_USER=demo

# Execute the Docker command
sudo docker exec -i $CONTAINER_NAME psql -U $PG_USER < $SQL_FILE


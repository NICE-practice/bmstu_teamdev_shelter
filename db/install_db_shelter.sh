#!/bin/bash

psql -h 127.0.0.1 "sslmode=disable user=postgres port=5432 password=1234" < ./create_db_shelter.sql

pip3 install psycopg2
pip3 install faker_vehicle
pip3 install faker
pip3 install random
pip3 install animals.py

python3 generate_db_shelter.py

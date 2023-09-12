import time
import random

from sqlalchemy import create_engine

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'

# Connect to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(
    db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

if __name__ == '__main__':
    print('Application started')

    while True:
        print('The last value inserted is: zero')
        time.sleep(5)

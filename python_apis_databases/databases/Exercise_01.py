'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
import sqlalchemy
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
engine = sqlalchemy.create_engine(f"mysql+pymysql://root:{PASSWORD}@localhost/sakila")

connection = engine.connect()
metadata = sqlalchemy.MetaData()
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)

# print(film.columns.keys())
print(metadata.tables['film'])
print(category.columns.name)

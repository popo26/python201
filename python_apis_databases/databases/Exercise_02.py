'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

'''
import sqlalchemy
from dotenv import load_dotenv
import os
from pprint import pprint



load_dotenv()

PASSWORD = os.getenv("PASSWORD")

engine = sqlalchemy.create_engine(f"mysql+pymysql://root:{PASSWORD}@localhost/sakila")

connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)

# - Select all the actors with the first name of your choice

# query = sqlalchemy.select([actor])
# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)

# - Select all the actors and the films they have been in

# join_film_actor = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
# query = sqlalchemy.select([film.columns.film_id, film.columns.title, actor.columns.first_name, actor.columns.last_name]).select_from(join_film_actor)
# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)

# - Select all the actors that have appeared in a category of a comedy of your choice

# query = sqlalchemy.select([film.columns.film_id, film.columns.title]).where(category.columns.category_id == '5')
# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchmany(3)
#pprint(result_set) # Ai picks (2, 'ACE GOLDFINGER')

#Ai:In progress

join1 = category.join(film_category.columns.category_id == category.columns.category_id).join(film.columns.film_id == film_category.columns.film_id)
join2 = actor.join(film_actor.columns.actor_id == actor.columns.actor_id).join(film_actor.columns.film_id == film.columns.film_id)
join = join1.join(join2)
query = sqlalchemy.select([actor.columns.first_name, actor.columns.last_name]).select_from(join1).where(film.columns.film_id == 2)
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
pprint(result_set)


# - Select all the comedic films and sort them by rental rate

# join1 = category.join(film_category, film_category.columns.category_id == category.columns.category_id).join(film, film.columns.film_id == film_category.columns.film_id)
# query = sqlalchemy.select([film.columns.title, film.columns.rental_rate]).select_from(join1).where(category.columns.category_id == 5).order_by(film.columns.rental_rate)
# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)

# - Using one of the statements above, add a GROUP BY statement of your choice

#Ai:In progress

# - Using one of the statements above, add a ORDER BY statement of your choice
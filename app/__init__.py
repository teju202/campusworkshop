"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaaem3hp8u791gtncn0-a.oregon-postgres.render.com",
        database="todo_2kv1",
        user="todo_2kv1_user",
        password="gd3u2k22nluXEyN10GdHTzg5YJZSqmDl")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

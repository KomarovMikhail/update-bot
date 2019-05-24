from queries import *
import psycopg2
from config import DATABASE_URL


def create_subscribes():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    cursor.execute(CREATE_SUBSCRIBES)
    conn.commit()
    conn.close()


def add_to_subscribes(cid):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    cursor.execute(EXISTS_SUBSCRIBES.format(cid))
    data = cursor.fetchall()
    if not data[0][0]:
        cursor.execute(INSERT_SUBSCRIBES.format(cid))
    conn.commit()
    conn.close()


def remove_from_subscribes(cid):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    cursor.execute(EXISTS_SUBSCRIBES.format(cid))
    data = cursor.fetchall()
    if data[0][0]:
        cursor.execute(DELETE_SUBSCRIBES.format(cid))
    conn.commit()
    conn.close()


def select_all_subscribes():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    cursor.execute(SELECT_SUBSCRIBES)
    data = cursor.fetchall()
    result = [item[0] for item in data]
    conn.commit()
    conn.close()
    return result

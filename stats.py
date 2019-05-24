from queries import *
import psycopg2
from config import DATABASE_URL
from spreadsheet import get_spreadsheet


def create_stats():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    cursor.execute(CREATE_STATS)
    conn.commit()
    conn.close()

    data = get_spreadsheet()
    for i, value in enumerate(data):
        add_to_stats(i, value)


def add_to_stats(i, value):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    cursor.execute(EXISTS_STATS.format(i))
    data = cursor.fetchall()
    if not data[0][0]:
        cursor.execute(INSERT_STATS.format(i, value))
    conn.commit()
    conn.close()


def compare_stats():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    cursor.execute(SELECT_STATS)
    data = cursor.fetchall()

    print(data)

    conn.commit()
    conn.close()


def remove_from_stats(i):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    cursor.execute(EXISTS_STATS.format(i))
    data = cursor.fetchall()
    if data[0][0]:
        cursor.execute(DELETE_STATS.format(i))
    conn.commit()
    conn.close()


def select_all_stats():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    cursor.execute(SELECT_SUBSCRIBES)
    data = cursor.fetchall()
    print(data)
    result = data[0]
    conn.commit()
    conn.close()
    return result

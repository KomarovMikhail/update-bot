from queries import *
import psycopg2
from config import DATABASE_URL, STATS_MAP
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
    conn.commit()
    conn.close()

    prev = [0, 0, 0, 0, 0, 0]
    for item in data:
        prev[item[0]] = item[1]
    curr = get_spreadsheet()
    result = []

    for i in range(len(prev)):
        if prev[i] == curr[i]:
            result.append(STATS_MAP[i] + ' >> Предыдущее значение: ' + str(prev[i]) + '. Текущее значение: ' +
                          str(curr[i]) + '.\n')
            update_stats(i, curr[i])

    return result


def update_stats(i, val):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    cursor.execute(UPDATE_STATS.format(i, val))
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

    cursor.execute(SELECT_STATS)
    data = cursor.fetchall()
    conn.commit()
    conn.close()

    curr = [0, 0, 0, 0, 0, 0]
    for item in data:
        curr[item[0]] = item[1]
    result = []
    for i in range(len(curr)):
        result.append(STATS_MAP[i] + ' >> ' + curr[i])
    return result

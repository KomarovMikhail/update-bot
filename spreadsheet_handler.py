from queries import *
from config import DATABASE_URL, SPREADSHEET_ID
import psycopg2


class SpreadsheetHandler:
    def __init__(self):
        self.cids = []

    def add_cid(self, cid):
        if cid in self.cids:
            return False
        self.cids.append(cid)
        return True

    def if_changing(self, cid):
        return cid in self.cids

    def remove_cid(self, cid):
        self.cids.remove(cid)


def create_link_storage():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    cursor.execute(CREATE_LINK_STORAGE)
    cursor.execute(INSERT_LINK_STORAGE.format(0, SPREADSHEET_ID))
    conn.commit()
    conn.close()


def update_link_storage(link):
    splited = link.split('/')
    if len(splited) < 6:
        return False
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    cursor.execute(UPDATE_LINK_STORAGE.format(0, splited[5]))
    conn.commit()
    conn.close()
    return True


def build_link():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    cursor.execute(SELECT_LINK_STORAGE)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data[0][1]

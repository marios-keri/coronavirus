import sqlite3
import scraper
import datetime

class Database:
    def __init__(self, db_location=None):
        self.DB_LOCATION = 'data.db'
        if db_location is not None:
            self.connection = sqlite3.connect(db_location)
        else:
            self.connection = sqlite3.connect(self.DB_LOCATION)

        self.cursor = self.connection.cursor()

    def insert(self, country, date, cases, deaths, recoverd):
        self.cursor.execute(f'INSERT OR IGNORE INTO {country} VALUES (?, ?, ?, ?)', (date, cases, deaths, recoverd))

    def create_table(self, country):
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {country} (date VARCHAR UNIQUE, cases VARCHAR, deaths VARCHAR, recoverd VARCHAR)""")

    def select(self, country, row):
        data = self.cursor.execute(f"""SELECT {row} FROM {country}""")
        return data

    def commit(self):
        self.connection.commit()


if __name__ == '__main__':
    coronavirus = scraper.Wikipedia()
    coronavirus_table = coronavirus.table

    database = Database('data.db')

    for countries in coronavirus.countries:
        database.create_table(countries.strip())

    for row in coronavirus.table:
        today = str(datetime.datetime.today())
        today = today.split(' ')[0]

        database.insert(row[0], today, row[1], row[2], row[3])

    database.commit()

    country = input('country : ').capitalize()
    row = input('cases, deaths, or recoverd : ').lower()

    data = database.select(country, row).fetchall()

    print(country, data)

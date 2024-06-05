import sqlite3

CONN = sqlite3.connect('pokemon.db')
CURSOR = CONN.cursor()

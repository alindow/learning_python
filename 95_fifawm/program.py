import sqlite3
import csv

from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return None

def create_table(conn, sql_ddl_statement):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param sql_ddl_statement: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_ddl_statement)
    except Error as e:
        print(e)

def load_nations(conn, filename):
    c = conn.cursor()
    with open(filename, 'r') as fin:
        # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [(i['name'], i['iaaf']) for i in dr]

    c.executemany("INSERT INTO nation (name, iaaf) VALUES (?, ?);", to_db)
    conn.commit()
    conn.close()


def main():
    database = "C:\\sqlite\db\pythonsql.db"
    nation = "teilnehmer.csv"

    sql_drop_nation = """ DROP TABLE nation; """
    sql_drop_spiel = """ DROP TABLE spiel; """
    sql_init_encoding = """PRAGMA encoding="UTF-8";"""

    sql_create_nation_table = """ CREATE TABLE IF NOT EXISTS nation (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            iaaf text NOT NUll
                                        ); """

    sql_create_spiel_table = """ CREATE TABLE IF NOT EXISTS spiel (
                                            nation1_id integer NOT NULL,
                                            nation2_id integer NOT NULL,
                                                 FOREIGN KEY (nation1_id) REFERENCES nation(id),
                                                 FOREIGN KEY (nation2_id) REFERENCES nation(id)
                                        ); """

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_drop_spiel)
        create_table(conn, sql_drop_nation)
        create_table(conn, sql_init_encoding)
        create_table(conn, sql_create_nation_table)
        create_table(conn, sql_create_spiel_table)
        load_nations(conn, nation)
        conn.close()



if __name__ == '__main__':
    main()

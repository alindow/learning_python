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

def create_sql_stmt(conn, sql_ddl_statement):
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

def load_groups(conn, filename):
    c = conn.cursor()
    with open(filename, 'r') as fin:
        # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [(i['name'], i['nation1'], i['nation2'], i['nation3'], i['nation4']) for i in dr]

    c.executemany("INSERT INTO gruppe (name, nation1, nation2,nation3,nation4) VALUES (?, ?, ?, ?, ?);", to_db)
    conn.commit()

def load_games(conn, filename):
    c = conn.cursor()
    with open(filename, 'r') as fin:
        # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        to_db = [(i['zeit'], i['nation1'], i['nation2'], i['tore1'], i['tore2']) for i in dr]

    c.executemany("INSERT INTO spiel (zeit, nation1, nation2, tore1, tore2) VALUES (?, ?, ?, ?, ?);", to_db)
    conn.commit()



def show_data(conn, sql_query):
    c = conn.cursor()
    try:
        c = conn.cursor()
        cursor = c.execute(sql_query)
        for row in cursor:
            print("name = {}".format(row[0]))
            for i in (1,2,3,4):
                print("nat = ", row[i])
            print()
    except Error as e:
        print(e)



def main():
    database = "C:\\sqlite\db\pythonsql.db"
    nation = "teilnehmer.csv"
    group = "gruppe.csv"
    game = "spiel.csv"

    sql_create_nation_table = """ CREATE TABLE IF NOT EXISTS nation (
                                            iaaf text PRIMARY KEY,
                                            name text NOT NULL
                                        ); """

    sql_create_gruppe_table = """ CREATE TABLE IF NOT EXISTS gruppe (
                                            name text NOT NULL,
                                            nation1 text NOT NULL,
                                            nation2 text NOT NULL,
                                            nation3 text NOT NULL,
                                            nation4 text NOT NULL,
                                                 FOREIGN KEY (nation1) REFERENCES nation(isaaf),
                                                 FOREIGN KEY (nation2) REFERENCES nation(isaaf),
                                                 FOREIGN KEY (nation3) REFERENCES nation(isaaf),
                                                 FOREIGN KEY (nation4) REFERENCES nation(isaaf)
                                        ); """

    sql_create_spiel_table = """ CREATE TABLE IF NOT EXISTS spiel (
                                            id integer PRIMARY KEY AUTOINCREMENT,
                                            zeit    datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
                                            nation1 text NOT NULL,
                                            nation2 text NOT NULL,
                                            tore1   integer NOT NULL DEFAULT 0,
                                            tore2   integer NOT NULL DEFAULT 0,
                                                 FOREIGN KEY (nation1) REFERENCES nation(isaaf),
                                                 FOREIGN KEY (nation2) REFERENCES nation(isaaf)
                                        ); """

    sql_show_groups = """ select gruppe.name, n1.name,n2.name,n3.name, n4.name 
                                 from gruppe 
                                 join nation as n1 on nation1 = n1.iaaf  
                                 join nation as n2 on nation2 = n2.iaaf 
                                 join nation as n3 on nation3 = n3.iaaf 
                                 join nation as n4 on nation4 = n4.iaaf
                                 ;"""


    conn = create_connection(database)
    if conn is not None:
        reset_db(conn)
        create_sql_stmt(conn, sql_create_nation_table)
        create_sql_stmt(conn, sql_create_spiel_table)
        create_sql_stmt(conn, sql_create_gruppe_table)
        load_nations(conn, nation)
        load_groups(conn, group)

        show_data(conn, sql_show_groups)

        load_games(conn, game)

        conn.close()


def reset_db(conn):
    sql_drop_nation = """ DROP TABLE nation; """
    sql_drop_spiel = """ DROP TABLE spiel; """
    sql_drop_gruppe = """ DROP TABLE gruppe; """
    sql_init_encoding = """PRAGMA encoding="UTF-8";"""

    create_sql_stmt(conn, sql_drop_spiel)
    create_sql_stmt(conn, sql_drop_nation)
    create_sql_stmt(conn, sql_drop_gruppe)
    create_sql_stmt(conn, sql_init_encoding)


if __name__ == '__main__':
    main()

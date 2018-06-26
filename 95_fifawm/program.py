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
        to_db = [(i['zeit'], i['nation1'], i['nation2'], i['tore1'], i['tore2'], i['gelb1'], i['gelb2'], i['rot1'], i['rot2']) for i in dr]

    c.executemany("INSERT INTO spiel (zeit, nation1, nation2, tore1, tore2, gelb1, gelb2, rot1, rot2)"
                  + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()



def show_groups(conn, sql_query):
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


def show_games(conn, sql_query):
    try:
        c = conn.cursor()
        cursor = c.execute(sql_query)
        for row in cursor:
            print("{}\t{} {} - {} {}".format(row[0], row[1], row[2], row[3], row[4]))
    except Error as e:
        print(e)


def show_list(conn, name):
    try:
        c = conn.cursor()
        cursor = c.execute("select nation1, nation2, nation3,nation4 from gruppe where name = '{}'".format(name))
        for nation in cursor:
            for i in range(4):
                print("nation[{}]: {}".format(i, nation[i]))
                cursor2 = c.execute("select nation1, nation2, tore1, tore2, gelb1,rot1,gelb2,rot2 from spiel where nation1 = '{}' or nation2 = '{}'".format(nation[i],nation[i]))
                punkte = 0
                tore = 0
                gegen_tore = 0
                gelb = 0
                rot = 0
                for row in cursor2:
                    print("{} - {}   {}:{}".format(row[0], row[1], row[2], row[3]))
                    if row[2] == row[3]:
                        punkte += 1
                        gegen_tore += row[2]
                        tore += row[3]
                        if row[0] == nation[i]:
                            gelb += row[4]
                            rot += row[5]
                        else:
                            gelb += row[6]
                            rot += row[7]
                    elif row[0] == nation[i] and row[2] > row[3]:
                        punkte += 3
                        tore += row[2]
                        gegen_tore += row[3]
                        gelb += row[4]
                        rot += row[5]
                    elif row[1] == nation[i] and row[3] > row[2]:
                        punkte += 3
                        tore += row[3]
                        gegen_tore += row[2]
                        gelb += row[6]
                        rot += row[7]
                    elif row[0] == nation[i]:
                        tore += row[2]
                        gegen_tore += row[3]
                        gelb += row[4]
                        rot += row[5]
                    elif row[3] == nation[i]:
                        tore += row[3]
                        gegen_tore += row[2]
                        gelb += row[6]
                        rot += row[7]

                print("Nation {} hat {} Punkte, {} Tore geschossen und {} Tore kassiert. Gelbe Karten: {}, rote Karten: {}".format(nation[i], punkte, tore, gegen_tore, gelb, rot))
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
                                            gelb1   integer NOT NULL DEFAULT 0,
                                            gelb2   integer NOT NULL DEFAULT 0,
                                            rot1    integer NOT NULL DEFAULT 0,
                                            rot2    integer NOT NULL DEFAULT 0,
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

    sql_show_games = """ select  spiel.zeit, n1.name, spiel.tore1, n2.name, spiel.tore2
                                 from spiel 
                                 join nation as n1 on nation1 = n1.iaaf  
                                 join nation as n2 on nation2 = n2.iaaf 
                                 ;"""



    conn = create_connection(database)
    if conn is not None:
        reset_db(conn)
        create_sql_stmt(conn, sql_create_nation_table)
        create_sql_stmt(conn, sql_create_spiel_table)
        create_sql_stmt(conn, sql_create_gruppe_table)
        load_nations(conn, nation)
        load_groups(conn, group)
        load_games(conn, game)

        show_groups(conn, sql_show_groups)
        show_games(conn, sql_show_games)

        show_list(conn, 'A')
        show_list(conn, 'B')
        show_list(conn, 'C')
        # show_list(conn, 'D')
        # show_list(conn, 'E')
        # show_list(conn, 'F')
        # show_list(conn, 'G')
        # show_list(conn, 'H')
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

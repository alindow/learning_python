import sqlite3
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

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "C:\\sqlite\db\pythonsql.db"

    sql_create_nation_table = """ CREATE TABLE IF NOT EXISTS nation (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL
                                        ); """

    sql_create_spiel_table = """ CREATE TABLE IF NOT EXISTS spiel (
                                            nation1_id integer NOT NULL,
                                            nation2_id integer NOT NULL,
                                                 FOREIGN KEY (nation1_id) REFERENCES nation(id),
                                                 FOREIGN KEY (nation2_id) REFERENCES nation(id)
                                        ); """

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_nation_table)
        create_table(conn, sql_create_spiel_table)
        conn.close()



if __name__ == '__main__':
    main()

import mysql.connector
from mysql.connector import Error
import json
import os
import Objects

def PrintConInfo(connection):
    if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Your connected to database: ", record[0])
            return cursor
    else:
        print("No Connection")
        return None

def ExecuteQuery(cursor,query):
    cursor.execute(query)
    
    return cursor.fetchall()

def ExecuteNonQuery(cursor,nonquery):
    cursor.execute(nonquery)

def LoadAllFromTable(cursor,table):
    query = (" SELECT * FROM " + table)

    return ExecuteQuery(cursor,query)

def LoadCards(cursor):
    pass

def PopulateTableList(cursor):
    query = """SELECT t.Table_Name
               FROM Information_Schema.TABLES t
               WHERE t.TABLE_SCHEMA = 'MagicTome'"""

    results = ExecuteQuery(cursor,query)

    tableLst = []

    # 0 - Cards
    # 1 - Card_Subtypes
    # 2 - Card_Types
    # 3 - Colors
    # 4 - Sets
    # 5 - SubTypes
    # 6 - Types

    for result in results:
        tbl = result[0]
        tableLst.append(tbl)

    return tableLst

def Main():
    try:
        
        with open('DatabaseConectionValues.json','r') as f:
            dbVars = json.load(f)

        connection = mysql.connector.connect(host=dbVars["host"],
                                            database=dbVars["database"],
                                            user=dbVars["user"],
                                            password=dbVars["password"])

        cursor = PrintConInfo(connection)


        # This is where the loop actually starts
        if cursor != None:
            cursor = connection.cursor()

    except Error as e:
        print("Error", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

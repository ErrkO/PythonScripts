import mysql.connector
from mysql.connector import Error
import json
import os
import Objects as Obj

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

def LoadCards(cursor,tableLst):
    return LoadAllFromTable(cursor,tableLst[0])

def LoadSets(cursor,tableLst):
    return LoadAllFromTable(cursor,tableLst[4])

def LoadColors(cursor,tableLst):
    return LoadAllFromTable(cursor,tableLst[3])

def LoadTypes(cursor,tableLst):
    return LoadAllFromTable(cursor,tableLst[6])

def LoadSubtypes(cursor,tableLst):
    return LoadAllFromTable(cursor,tableLst[5])

def LoadCardTypes(cursor,cardID,tableLst):
    return LoadAllFromTable(cursor,tableLst[1])

def LoadCardSubtypes(cursor,cardID,tableLst):
    return LoadAllFromTable(cursor,tableLst[2])

def SaveCards(cursor,cards):
    for card in cards:
        SaveCard(cursor,card)

def SaveCard(cursor,card):
    query = ("""INSERT INTO Cards(
              CardID
	          ,CMC
	          ,ManaCost
	          ,NAME
	          ,Power
	          ,Rarity
	          ,SetID
	          ,Text
	          ,Toughness
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s)""")

    record = cursor.execute(query,card.Parameterize())

    return record

def SaveSets(cursor,sets):
    for set in sets:
        SaveSet(cursor,set)

def SaveSet(cursor,set):
    query = ("""INSERT INTO Sets(
                     SetID
                    ,SetCode
                    ,SetName)
                Values
                    (%s,%s,%s)""")
    
    record = cursor.execute(query,set.Parameterize())

    return record

def SaveTypes(cursor,tableLst):
    return LoadAllFromTable(cursor,tableLst[6])

def SaveSubtypes(cursor,tableLst):
    return LoadAllFromTable(cursor,tableLst[5])

def SaveCardTypes(cursor,cardID,tableLst):
    return LoadAllFromTable(cursor,tableLst[2])

def SaveCardSubtypes(cursor,cardID,tableLst):
    return LoadAllFromTable(cursor,tableLst[1])

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


Main()
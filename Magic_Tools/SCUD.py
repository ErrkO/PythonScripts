import mysql.connector
from mysql.connector import Error
import json
import os
import Objects as Obj
import MagicApiHandler as Handler

#Standard2019 = ['xln','rix','dom','m19','grn','rna','war','m20']
#Standard2020 = ['grn','rna','war','m20','eld','thb','iko']
SetsInArena = ['XLN','RIX','DOM','M19','GRN','RNA','WAR','M20','ELD','THB','IKO']

def BuildBaseDB(connection,cursor):

    print('Saving all the Sets')
    sets = Handler.GetAllSets()
    SaveSets(cursor,sets)

    print('\nSaving all the Types')
    types = Handler.GetAllTypes()
    SaveTypes(cursor,types)

    print('\nSaving all the Subtypes')
    subtypes = Handler.GetAllSubtypes()
    SaveSubtypes(cursor,subtypes)

    print('\nSaving all the SuperTypes')
    supertypes = Handler.GetAllSupertypes()
    SaveSupertypes(cursor,supertypes)

    for seta in sets:
        for setb in SetsInArena:
            if seta.SetCode == setb:
                print('Saving set: ' + seta.SetName)
                cards = Handler.GetAllCardsInSet(seta.SetCode)
                SaveCards(cursor,cards)

    connection.commit()

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
	           CMC
              ,ImageURL
	          ,ManaCost
	          ,NAME
              ,Number
	          ,Power
	          ,Rarity
	          ,SetCode
	          ,Text
	          ,Toughness
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""")

    cursor.execute(query,card.Parameterize(True))

def SaveSets(cursor,sets):
    for sett in sets:
        InsertSet(cursor,sett)

def InsertSet(cursor,sett):
    query = ("""INSERT INTO Sets(
                     SetCode
                    ,SetName)
                Values
                    (%s,%s)""")
    
    record = cursor.execute(query,sett.Parameterize())

    return record

def SaveTypes(cursor,types):
    for typee in types:
        InsertType(cursor,typee)

def InsertType(cursor,typee):
    query = ("""INSERT INTO Types(
                     TypeDesc
                    )
                Values
                    (%s)""")
    
    record = cursor.execute(query,typee.Parameterize(True))

    return record

def SaveSubtypes(cursor,subtypes):
    for sub in subtypes:
        InsertSubtype(cursor,sub)

def InsertSubtype(cursor,sub):
    query = ("""INSERT INTO Subtypes(
                     SubtypeDesc
                    )
                Values
                    (%s)""")
    
    record = cursor.execute(query,sub.Parameterize(True))

    return record

def SaveSupertypes(cursor,supertypes):
    for sup in supertypes:
        InsertSupertype(cursor,sup)

def InsertSupertype(cursor,sup):
    query = ("""INSERT INTO Supertypes(
                     SupertypeDesc
                    )
                Values
                    (%s)""")
    
    record = cursor.execute(query,sup.Parameterize(True))

    return record

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
        
        with open('F:\\Users\\erico\\Code_Projects\\PythonScripts\\Magic_Tools\\DatabaseConectionValues.json','r') as f:
            dbVars = json.load(f)

        connection = mysql.connector.connect(host=dbVars["host"],
                                            database=dbVars["database"],
                                            user=dbVars["user"],
                                            password=dbVars["password"])

        cursor = PrintConInfo(connection)

        # This is where the loop actually starts
        if cursor != None:
            cursor = connection.cursor()

            BuildBaseDB(connection,cursor)
            
    except Error as e:
        print("Error", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

Main()

import sqlite3
import os
from team_manager.helpers.debugger import p
import django_tables2 as tables

default_db_name = "main.db"
default_table_name = "contacts"
current_file_name = os.path.abspath(__file__)
current_folder = os.path.dirname(current_file_name)
data_model = [
                ("id","INTEGER  PRIMARY KEY  AUTOINCREMENT"),
                ("first_name","TEXT NOT NULL"),
                ("second_name","name TEXT NOT NULL"),
                ("email","name TEXT NOT NULL"),
                ]
 
data_model_str = ", ".join([" ".join(el) for el in data_model ]) 
#print(data_model_str)
#data_model_str  = """
#        id INTEGER  PRIMARY KEY  AUTOINCREMENT,
#        first_name TEXT NOT NULL,
#        second_name TEXT NOT NULL,
#        email TEXT NOT NULL
#        """

dummy_entries = [
        (None,"Olivia","Li","olivia@li.de"),
        (None,"Jack","Jonson","jack@jonson.com"), 
        (None,"Jan","Jannsen","jan@jannsen.de"), 
        (None,"Ameli","Xerox","ameli@xerox.de"), 
        #(None,"","",""), 
        #(None,"","",""),    
        ]



class DBHandler(object):

    def __init__(self):
        self.conn = None 


    def __del__(self):
        if self.conn:
            self.conn.close()


    def create_db(self,db_file):
        """ create a db file """
        self.db_file = db_file
        try:
            if os.path.isfile(self.abs_paht_to_db_file):
                raise Exception("Given db_file ('{}') is already exist".format(self.db_file))

            self.conn = sqlite3.connect(self.abs_paht_to_db_file)
            if self.conn and os.path.isfile(self.abs_paht_to_db_file):
                print("------>>>>DB was created<<<<<-------")
            print(sqlite3.version)
            self.create_default_data_model()
        except Exception as e:
            print(e)
        #finally:
        #    self.conn.close()


    def cols(self,table_name):
        cur = self.conn.cursor()
        qeary1 = "PRAGMA table_info({})"
        qeary2 = """
        SELECT sql FROM sqlite_master
        WHERE tbl_name = '{}' AND type = 'table'
        """
        res = cur.execute(qeary1.format(table_name))
        
        colnames = [elem[1] for elem in res.fetchall()]
        return colnames





    def tables(self):
        cur = self.conn.cursor()
        res = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for name in res:
            yield name[0]



    def create_default_data_model(self):
        if default_table_name in self.tables():
            raise Exception('{}-Table is already exist!!!'.format(default_table_name))
        try:
            query = "CREATE TABLE contacts ( {} );".format(data_model_str )
            #p(repr(query))
            #p(query)
            #query = [line.replace("  ","") for line in query.split('\n')]
            #query = " ".join(query)
            #p(query,"query")
            cur = self.conn.cursor()
            cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(repr(e))

        if default_table_name not in self.tables():
            raise Exception('{}-Table wasnt created!!!'.format(default_table_name))

        if set(self.cols(default_table_name) ) != set([el[0] for el in data_model ]):
            raise Exception('{}-Table has wrong colnames!!!'.format(default_table_name))


        print("------>>>Data Model  was created<<<<<-------")

        self.add_dummy_entries()
        rownum = len(list(self.rows(default_table_name)))
        if len(dummy_entries) != rownum:
            raise Exception('{}-Table dummy items wasnt inserted!!!'.format(default_table_name))

        print("------>>>Dummy Items  was inserted<<<<<-------")





    def connect(self,db_file):
        """ create a database connection to a SQLite database """
        self.db_file = db_file
        #p((current_folder, self.db_file))
        self.abs_paht_to_db_file = os.path.join(current_folder, self.db_file)
        try:
            if not os.path.isfile(self.abs_paht_to_db_file):
                #print(os.path.abspath(__file__))
                #p(current_folder)
                #raise Exception("Given db_file ('{}') is not exist".format(db_file))
                self.create_db(self.abs_paht_to_db_file)
            else:
                self.conn = sqlite3.connect(self.abs_paht_to_db_file)

            print(sqlite3.version)

            #p(list(self.tables()))
            if default_table_name not in self.tables():
                #p(self.conn)
                self.conn.close()
                self.conn = None
                #self = DBHandler()
                os.remove(self.abs_paht_to_db_file)
                raise Exception('{}-Table wasnt found!!!'.format(default_table_name))
            #print(self.cols(default_table_name))
            #p()
            
        except Exception as e:
            print(e)
        #finally:
        #    self.conn.close()

    def add_dummy_entries(self):
        #self.conn  = 
        cols = self.cols("contacts")
        colnames = ", ".join(cols)
        placeholder = ", ".join(["?" for c in cols])
        query = """
                INSERT INTO  {} ({})
                VALUES ({});
            """
        #for 
        #p(query.format(colnames, placeholder))
        cur = self.conn.cursor()
        res = cur.executemany(query.format(default_table_name,colnames, placeholder),dummy_entries)
        self.conn.commit()


    def rows(self, table_name):
        cur = self.conn.cursor()
        res = cur.execute("SELECT * FROM {}".format(table_name))
        for row in res.fetchall():
            yield row



db_handler = DBHandler()

def connect(db_file):
    connect = db_handler.connect(db_file)
    return connect


def getTable(table_name):
    conn = connect(default_db_name)
    cursor = db_handler.conn.cursor()
    #p(cursor )
    #try:
    cursor.execute("""SELECT * FROM %s;""" %(table_name)) # want autoincrement key?
    exptData = dictfetchall(cursor)
        #p(exptData)
    #except Exception as e:
    #    ''      

    attrs = {}
    cols=exptData[0]

    for item in cols:
        attrs[str(item)] = tables.Column()

    myTable = type('myTable', (tables.Table,), attrs)        

    return myTable(exptData)

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    #p(desc)
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]   



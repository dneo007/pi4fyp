import sqlite3 as sqlite3

def dbqueryreading():

    try:
        db = sqlite3.connect('/home/pi/Desktop/flask_app/flaskapp/site.db') #DB connection
        db.row_factory = lambda cursor, row: row[0]
        cursor = db.cursor() #Create cursor object
        sensedata = cursor.execute('SELECT results FROM reading ORDER BY date_posted DESC LIMIT 10').fetchall()
        return sensedata
    except Exception as e:
        raise e
    finally:
        db.close()

def dbquerydate():

    try:
        db = sqlite3.connect('/home/pi/Desktop/flask_app/flaskapp/site.db') #DB connection
        db.row_factory = lambda cursor, row: row[0]
        cursor = db.cursor() #Create cursor object
        sensedata = cursor.execute('SELECT date_posted FROM reading ORDER BY date_posted DESC LIMIT 10').fetchall()
        return sensedata
    except Exception as e:
        raise e
    finally:
        db.close()

def dbqueryreadingall():

    try:
        db = sqlite3.connect('/home/pi/Desktop/flask_app/flaskapp/site.db') #DB connection
        db.row_factory = lambda cursor, row: row[0]
        cursor = db.cursor() #Create cursor object
        sensedata = cursor.execute('SELECT results FROM reading ORDER BY date_posted DESC').fetchall()
        return sensedata
    except Exception as e:
        raise e
    finally:
        db.close()


def dbquerydateall():
    try:
        db = sqlite3.connect('/home/pi/Desktop/flask_app/flaskapp/site.db') #DB connection
        db.row_factory = lambda cursor, row: row[0]
        cursor = db.cursor() #Create cursor object
        sensedata = cursor.execute('SELECT date_posted FROM reading ORDER BY date_posted DESC').fetchall()
        return sensedata
    except Exception as e:
        raise e
    finally:
        db.close()

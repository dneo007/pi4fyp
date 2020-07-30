import sqlite3 as sqlite3
from datetime import datetime, timedelta

def dbqueryreading(type):

    try:
        db = sqlite3.connect('/home/pi/Desktop/flask_app/flaskapp/site.db') #DB connection
        db.row_factory = lambda cursor, row: row[0]
        cursor = db.cursor() #Create cursor object
        if type == 'latest':
            sensedata = cursor.execute('SELECT results FROM reading ORDER BY date_posted DESC LIMIT 10').fetchall()
        elif type == 'all':
            sensedata = cursor.execute('SELECT results FROM reading ORDER BY date_posted DESC').fetchall()
        elif type == 'week':
            period= datetime.now() - timedelta(weeks=1)
            sensedata = cursor.execute('SELECT results FROM reading WHERE date_posted > ? ORDER BY date_posted DESC', (period.strftime("%d-%m-%Y %H:%M:%S"),)).fetchall()
        elif type == 'month':
            period= datetime.now() - timedelta(weeks=4)
            sensedata = cursor.execute('SELECT results FROM reading WHERE date_posted > ? ORDER BY date_posted DESC', (period.strftime("%d-%m-%Y %H:%M:%S"),)).fetchall()
        return sensedata
    except Exception as e:
        raise e
    finally:
        db.close()

def dbquerydate(type):

    try:
        db = sqlite3.connect('/home/pi/Desktop/flask_app/flaskapp/site.db') #DB connection
        db.row_factory = lambda cursor, row: row[0]
        cursor = db.cursor() #Create cursor object
        if type == 'latest':
            sensedata = cursor.execute('SELECT date_posted FROM reading ORDER BY date_posted DESC LIMIT 10').fetchall()
        elif type == 'all':
            sensedata = cursor.execute('SELECT date_posted FROM reading ORDER BY date_posted DESC').fetchall()
        elif type == 'week':
            period= datetime.now() - timedelta(weeks=1)
            sensedata = cursor.execute('SELECT date_posted FROM reading WHERE date_posted > ? ORDER BY date_posted DESC', (period.strftime("%d-%m-%Y %H:%M:%S"),)).fetchall()
        elif type == 'month':
            period= datetime.now() - timedelta(weeks=4)
            sensedata = cursor.execute('SELECT date_posted FROM reading WHERE date_posted > ? ORDER BY date_posted DESC', (period.strftime("%d-%m-%Y %H:%M:%S"),)).fetchall()
        return sensedata
    except Exception as e:
        raise e
    finally:
        db.close()

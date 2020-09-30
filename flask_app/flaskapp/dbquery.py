import sqlite3 as sqlite3
from datetime import datetime, timedelta
from flaskapp.dbentry2 import dbinsertmax

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

def dbquerymax(type):

    try:
        db = sqlite3.connect('/home/pi/Desktop/flask_app/flaskapp/site.db') #DB connection
        cursor = db.cursor() #Create cursor object
        checkexists = 1
        if type == 'latest':
            period= datetime.now() - timedelta(days=1000)
            max = cursor.execute('SELECT MAX(results),date_posted FROM reading WHERE date_posted > ? ', (period.strftime("%d-%m-%Y %H:%M:%S"),)).fetchone()
            if max[0] != None:
                #check if entry already exists
                checkexists = cursor.execute('SELECT MAX(results) FROM max_reading WHERE date_posted > ? ', (period.strftime("%d-%m-%Y %H:%M:%S"),)).fetchone()[0]
                if checkexists is None:
                    checkexists = 0
#                    print("insert into max_readings " + str(max[0])+ ", " + str(max[1]))
                    cursor.execute('''INSERT INTO max_reading(results,date_posted) VALUES(?,?)''', (max[0], max[1],))
                    db.commit()
                else:
                    print("ROW ALREADY EXISTS")
                    # db.close()
            #if value is not none
            #query for values for 1 day before, if NONE values returned then insert max to table
        elif type == 'all':
            max = cursor.execute('SELECT MAX(results),date_posted FROM reading').fetchone()
        elif type == 'week':
            period= datetime.now() - timedelta(weeks=1)
            max = cursor.execute('SELECT MAX(results),date_posted FROM reading WHERE date_posted > ? ', (period.strftime("%d-%m-%Y %H:%M:%S"),)).fetchone()
        elif type == 'month':
            period= datetime.now() - timedelta(weeks=4)
            max = cursor.execute('SELECT MAX(results),date_posted FROM reading WHERE date_posted > ? ', (period.strftime("%d-%m-%Y %H:%M:%S"),)).fetchone()
        print(max[1])
        maxdata = {
        'max': max[0],
        'date': max[1],
        }
        return maxdata
    except Exception as e:
        raise e
    finally:
        db.close()

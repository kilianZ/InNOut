import sqlite3

class User():
    def __init__(self, username, password):
        self.username = username 
        self.password = password
        conn = sqlite3.connect('users.db')
        c = conn.cursor() 
        c.execute('''CREATE TABLE IF NOT EXISTS users(
                  username VARCHAR(255), 
                  password VARCHAR(255));''')
        conn.commit()
        conn.close() 
        
    def signIn(self):
        # open/create .db file 
        conn = sqlite3.connect('users.db')
        c = conn.cursor() 
        c.execute('''SELECT * FROM users
                  WHERE username = '{}';'''.format(self.username))
        response = c.fetchall() 
        conn.close() # close .db file 
        if len(response) > 0:
            if (self.password == response[0][1]):
                return (True, True) 
            else: 
                return (True, False)
        return (False, False)
        



'''
models.py 
contains Database Models (Sqlite tables as python classes) 
'''


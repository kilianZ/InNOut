import sqlite3

class User():
    def __init__(self, username, password):
        self.username = username 
        self.password = password
        conn = sqlite3.connect('users.db')
        c = conn.cursor() 
        c.execute('''CREATE TABLE IF NOT EXISTS users(
                  username VARCHAR(255) PRIMARY KEY, 
                  password VARCHAR(255));''')
        conn.commit()
        conn.close() 

    def genUserID(self):
        # open/create .db file 
        conn = sqlite3.connect('users.db')
        c = conn.cursor() 
        c.execute('''SELECT * FROM users;''') 
        response = c.fetchall() 
        conn.close() # close .db file 
        return len(response)
        
    def signIn(self):
        # open/create .db file 
        conn = sqlite3.connect('users.db')
        c = conn.cursor() 
        c.execute('''SELECT * FROM users
                  WHERE username = '{}';'''.format(self.username))
        response = c.fetchall() 
        print(response) 
        conn.close() # close .db file 
        if len(response) > 0:
            if (self.password == response[0][1]):
                return (True, True) 
            else: 
                return (True, False)
        return (False, False)
    
    def signUp(self):
        # open/create .db file 
        conn = sqlite3.connect('users.db')
        c = conn.cursor() 
        c.execute('''INSERT INTO users
                  VALUES('{}', '{}');
                  '''.format(self.username, self.password))
        conn.commit()
        conn.close() # close .db file 




'''
models.py 
contains Database Models (Sqlite tables as python classes) 
'''


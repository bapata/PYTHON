import sqlite3
createDB=sqlite3.connect(':memory:')
queryCurs=createDB.cursor()

def createTable():
  queryCurs.execute('''CREATE TABLE customers
  (id INTEGER PRIMARY KEY, name TEXT, street TEXT, city TEXT, state TEXT , balance REAL)''')

def addCust(name,street,city,state,balance):
  queryCurs.execute('''INSERT INTO customers (name,street,city,state,balance) 
  VALUES (?,?,?,?,?)''',(name,street,city,state,balance))

def main():
  createTable()
  addCust('Anand Bapat','10250','cupertino','CA',1.1)
  addCust('Ajita Bapat','10250','cupertino','CA',2.2)
  createDB.commit()
  queryCurs.execute('SELECT * FROM customers')

  for i in queryCurs:
    print "\n"
    for j in i:
      print j

if __name__ == '__main__':
  main()

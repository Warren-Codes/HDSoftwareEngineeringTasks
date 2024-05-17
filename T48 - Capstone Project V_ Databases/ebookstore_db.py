import sqlite3
db = sqlite3.connect('data/ebookstore_db')
cursor = db.cursor()  # Get a cursor object

cursor.execute('''
    CREATE TABLE books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT,
                   	Qty INTEGER)
''')
db.commit()

# Creates books
cursor = db.cursor()
id1 = 3001
Title1 = 'A Tale of Two Cities'
Author1 = 'Charles Dickens'
Qty1 = 30


id2 = 3002
Title2 = 'Harry Potter and the Philosopher\'s Stone'
Author2 = 'J.K. Rowling'
Qty2 = 40


id3 = 3003
Title3 = 'The Lion, The Witch and the Wardrobe'
Author3 = 'C.S. Lewis'
Qty3 = 25


id4 = 3004
Title4 = 'The Lord of the Rings'
Author4 = 'J.R.R. Tolkien'
Qty4 = 37


id5 = 3005
Title5 = 'Alice in Wonderland'
Author5 = 'Lewis Carroll'
Qty5 = 12

# Insert book 1
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                  VALUES(?,?,?,?)''', (id1, Title1, Author1, Qty1))
print('First book inserted.')

# Insert book 2
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                  VALUES(?,?,?,?)''', (id2, Title2, Author2, Qty2))
print('Second book inserted.')

# Insert book 3
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                  VALUES(?,?,?,?)''', (id3, Title3, Author3, Qty3))
print('Third book inserted.')

# Insert book 4
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                  VALUES(?,?,?,?)''', (id4, Title4, Author4, Qty4))
print('Fourth book inserted.')

# Insert book 4
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                  VALUES(?,?,?,?)''', (id5, Title5, Author5, Qty5))
print('Fifth book inserted.')
db.commit()

# This will show the contents of the db within the IDE terminal. These have been commented out so they are not in the main ebookstore_db
# print('SELECT id, Book Title, Book Author, Book Qty FROM books:')
# cursor.execute('''SELECT id, Title, Author, Qty FROM books WHERE Qty BETWEEN 1 AND 80''')
# for row in cursor:
#     # row[0] returns id column, row[1] returns name column, row[2] returns grade column.
#     print('Book ID: {0}\t  Book Name: {1}\t \t\t   Book Author: {2}\t     Book Qty: {3}\t'.format(row[0], row[1], row[2], row[3]))


db.commit()
db.close()
print('Connection to ebookstore database closed.')



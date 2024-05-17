import sqlite3
db = sqlite3.connect('data/python_programming_db')
cursor = db.cursor()  # Get a cursor object

cursor.execute('''
    CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT,
                   	grade INTEGER)
''')
db.commit()

# Creates students
cursor = db.cursor()
id1 = 55
name1 = 'Carl Davis'
grade1 = 61


id2 = 66 
name2 = 'Dennis Fredrickson'
grade2 = 88


id3 = 77
name3 = 'Jane Richards'
grade3 = 78


id4 = 12
name4 = 'Peyton Sawyer'
grade4 = 45


id5 = 2
name5 = 'Lucas Brooke'
grade5 = 99

# Insert student 1
cursor.execute('''INSERT INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', (id1, name1, grade1))
print('First user inserted.')

# Insert student 2
cursor.execute('''INSERT INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', (id2, name2, grade2))
print('Second user inserted.')

# Insert student 3
cursor.execute('''INSERT INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', (id3, name3, grade3))
print('Third user inserted.')

# Insert student 4
cursor.execute('''INSERT INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', (id4, name4, grade4))
print('Fourth user inserted.')

# Insert student 5
cursor.execute('''INSERT INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', (id5, name5, grade5))
print('Fifth user inserted.')
db.commit()

print('SELECT id, name, grade FROM python_programming:')
cursor.execute('''SELECT id, name, grade FROM python_programming WHERE grade BETWEEN 60 AND 80''')
for row in cursor:
    # row[0] returns id column, row[1] returns name column, row[2] returns grade column.
    print('Student ID: {0}   Student Name: {1}    Student Grade: {2}'.format(row[0], row[1], row[2]))

# Updates Carl Davis, id 55 to grade 65
grade = 65
id = 55
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id = ? ''', (grade, id))
print('Student data updated!')


# Delete Dennis Frederickson with id 66
id = 66
cursor.execute('''DELETE FROM python_programming WHERE id = ? ''', (id,))
print('Student %d deleted.' %id)


# Updates all grades to 72 where the id is below 55
cursor.execute('''UPDATE python_programming SET grade = 72 WHERE id < 55''')
print('Student data updated!')


db.commit()
db.close()
print('Connection to database closed.')



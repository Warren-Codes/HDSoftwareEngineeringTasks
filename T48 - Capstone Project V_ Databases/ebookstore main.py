import sqlite3

OKGREEN = '\033[92m'

# connect_to_db function connects to the ebookstore_db
def connect_to_db():
    db=sqlite3.connect('data/ebookstore_db')
    cursor=db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT,
                   	Qty INTEGER)''')
    db.commit()
    db.close()


# add_new function asks the user to input the id, title, author and qty of a new book. This then gets commited to the ebookstore_db
def add_new():
    id, Title, Author, Qty = input(f"{OKGREEN}id, Title, Author, Qty ").split(",")
    db=sqlite3.connect('data/ebookstore_db')
    cursor=db.cursor()
    cursor.execute("INSERT INTO books VALUES (?,?,?,?)",(id, Title, Author, Qty))
    db.commit()
    db.close()
    print(view_books())


# view_books function shows all of the books in the ebookstore_db in a user friendly way by using the for loop
def view_books():
    db=sqlite3.connect('data/ebookstore_db')
    cursor=db.cursor()
    cursor.execute("SELECT * FROM books")
    rows=cursor.fetchall()
    db.close()
    
    for row in rows:
        print(row)
    
    
# update_book function asks the user to input the id, title, author and qty of a book they would like to update. This then gets commited to the ebookstore_db
def update_books():
    id, Title, Author, Qty = input("id, Title, Author, Qty ").split(",")
    db=sqlite3.connect('data/ebookstore_db')
    cursor=db.cursor()
    cursor.execute("UPDATE books SET Title=?, Author=?, QTY=? WHERE id=?",(Title, Author, Qty, id))
    db.commit()
    db.close()
    print(view_books())



# delete_books function asks the user to input the id of the book the book they would like to delete. This then gets commited to the ebookstore_db
def delete_books():
    id = int(input("id "))
    db=sqlite3.connect('data/ebookstore_db')
    cursor=db.cursor()
    cursor.execute("DELETE FROM books WHERE id=?",(id,))
    db.commit()
    db.close()



# search_books function asks the user to input the title and author of the book they would like to search. This gets presented to the author in a user friendly way using the for loop.
def search_books():
    Title, Author = input("Title, Author ").split(",")
    db=sqlite3.connect('data/ebookstore_db')
    cursor=db.cursor()
    cursor.execute("SELECT * FROM books WHERE Title=? OR Author=?", (Title, Author))
    rows=cursor.fetchall()
    db.close()
    for row in rows:
        print(row)
    return rows
    


def menu():
    print(f"{OKGREEN}\n1. Add new book")
    print(f"{OKGREEN}2. Update book")
    print(f"{OKGREEN}3. Delete book")
    print(f"{OKGREEN}4. Search books")
    print(f"{OKGREEN}5. View books")
    print(f"{OKGREEN}0. Exit")
    print()



connect_to_db()


# Main program displays the menu and calls the relevant functions based on the user input. The while loop breaks when the user types in '0' to exit.
while True:
    menu()
    user_input = input(f"{OKGREEN}Please select an option: ")

    if user_input == "1":
        add_new()

    elif user_input == "2":
        update_books()

    elif user_input == "3":
        delete_books()

    elif user_input == "4":
        search_books()

    elif user_input == "5":
        view_books()

    elif user_input == "0":
        print(f"{OKGREEN}Logging off...\n")
        break
        
    else:
        print(f"{OKGREEN}\nPlease select a valid option")
        continue
    



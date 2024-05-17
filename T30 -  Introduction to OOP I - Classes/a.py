# This program is an email simulator in which it lets the user send emails and view emails.

# The text in the console will be green! :)
OKGREEN = '\033[92m'

# Email class is created with a range of variables and methods
class Email:
    email_contents = []
    has_been_read = False
    is_spam = False
    from_address = []

    # method which initialises a range of attributes - an email address and then has_been_read and is_spam are
    # assigned with the False boolean
    def __init__(self, e_mail_address, has_been_read=False, is_spam=False):
        self.e_mail_address = e_mail_address
        self.has_been_read = has_been_read
        self.is_spam = is_spam

    # mark_as_read method turns the has_been_read boolean to True
    def mark_as_read(self):
        self.has_been_read = True

    # mark_as_spam method turns the is_spam boolean to True
    def mark_as_spam(self):
        self.is_spam = True

    # __str__ method returns the data as a string instead of the place in computer memory where it is stored
    def __str__(self):

        return f"{OKGREEN}{self.e_mail_address}, {self.has_been_read}, {self.is_spam}"

    # __repr__ represents data in a string as opposed to an object with random information where the object is stored
    def __repr__(self):
        return f"{self.e_mail_address!r}, {self.has_been_read!r}, {self.is_spam!r}"

# Global variable that will store the inbox emails in a list
inbox = []


# functions #
# add_email function asks the user to input an email address and email contents. This is stored in two separate lists
# with a third result list being created which holds both the email and contents. This is appended to the inbox list
def add_email():
    email = Email(input(f"{OKGREEN}What is your e-mail address: "))
    contents = input(f"{OKGREEN}Please compose your email message: ")
    Email.from_address.append(email)
    Email.email_contents.append(contents)
    result = [email, contents]
    inbox.append(result)


# all_emails function loops through the items in inbox and prints each email and its contents on a new line
def all_emails():
    for num, email in enumerate(inbox, start=1):
        print(f"{OKGREEN}Number {num}  email is: {email}")


# get_count function takes the length of the inbox list and prints out how many emails are in the list
def get_count():
    email_count = len(inbox)
    print(f"{OKGREEN}There are {email_count} emails in your inbox.")


# get_email function calls the all_email function so it can view all emails. The user is then asked to input which
# email index they would like to view, which uses the email mark_as_read method to turn the read boolean to True
def get_email():
    all_emails()
    question = input(f"{OKGREEN}What email would you like to view? ")
    if int(question) in range(1, len(inbox)+1):
        email_instance = inbox[int(question) - 1][0]
        email_instance.mark_as_read()
        print(inbox[int(question) - 1])
        return inbox[int(question) - 1]

    else:
        print("Invalid email number.")


# get_unread_emails function loops through the inbox list, starting at 1. If the email is not.has_been_read then it
# prints all of the False emails
def get_unread_emails():
    for num, email in enumerate(inbox, start=1):
        if not email[0].has_been_read:
            print(f"Number {num} unread email is: {email}")


# spam_emails function loops through the inbox list, starting at 1. If the email spam boolean is True then it
# prints all of the True emails
def spam_emails():
    for num, email in enumerate(inbox, start=1):
        if email[0].is_spam:
            print(f"Number {num} spam email is: {email}")


# mark_spam function calls the all_emails function so the user can view all emails. The user is then asked to input the
# number of the email they would like to mark as spam. The mark_as_spam method is called which turns the if_spam
# attribute to True
def mark_spam():
    all_emails()
    question = input(f"{OKGREEN}What email would you like to mark as spam? ")
    if int(question) in range(1, len(inbox) + 1):
        spam_instance = inbox[int(question) - 1][0]
        spam_instance.mark_as_spam()
        return inbox[int(question) - 1]

    else:
        print(f"{OKGREEN}Invalid email number.")


# delete function calls the all_emails function so the user can view all emails. They are then asked to input the
# number of the email they would like to delete. This email is then deleted.
def delete():
    all_emails()
    question = input(f"{OKGREEN}What email would you like to delete? ")
    if int(question) in range(1, len(inbox) + 1):
        email_to_delete = inbox[int(question) - 1]
        index_to_delete = inbox.index(email_to_delete)
        print(f"{OKGREEN}Email deleted.")
        del inbox[index_to_delete]


# read_menu function prints out the menu for when the user types in 'read'
def read_menu():
    print(f"\n{OKGREEN}Type in the corresponding number for what you would like to read:")
    print(f"{OKGREEN}1 - All emails.")
    print(f"{OKGREEN}2 - Unread emails.")
    print(f"{OKGREEN}3 - Spam emails.")
    print(f"{OKGREEN}4 - Index specific email.")


user_choice = f"{OKGREEN}"

# while loop which runs until the user types in 'quit'. This is the main program which calls on the previous methods
# and functions
while user_choice.lower() != "quit":
    user_choice = input(f"{OKGREEN}\nWhat would you like to do - read/get count/mark spam/send/delete/quit? \n")
    if user_choice.lower() == "read":
        read_menu()
        read_choice = (input(f"{OKGREEN}"))
        if read_choice == "1":
            all_emails()
        elif read_choice == "2":
            get_unread_emails()
        elif read_choice == "3":
            spam_emails()
        elif read_choice == "4":
            get_email()
        else:
            print(f"{OKGREEN}You did not make a valid choice.")

    elif user_choice.lower() == "get count":
        get_count()
    elif user_choice.lower() == "mark spam":
        mark_spam()
    elif user_choice.lower() == "send":
        add_email()
    elif user_choice.lower() == "delete":
        delete()
    elif user_choice.lower() == "quit":
        print(f"{OKGREEN}Goodbye")
    else:
        print(f"{OKGREEN}Oops - incorrect input")

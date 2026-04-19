# ===============================================================LIBRARY MANAGEMENT SYSTEM ===============================================================
#  DATABASE
print("===========================================================WELCOME TO OUR LIBRARY=======================================================")
books = []
issued_books = []
def add_book():
    name = input('Enter the book Name: ')
    books.append(name)
    print(f'{name} is added')

def show_books():
    if len(books) == 0:
        print('No books Available')
    else:
        print("Books Available:")
        for book in books:
            print(book)

def issue_book():
    if len(books) == 0:
        print("No books Available")
        return
    show_books()
    user_want = input("Enter the book name: ")
    if user_want in books:
        print(user_want,"Issued")
        issued_books.append(user_want)
        books.remove(user_want)
    else:
        print("Please enter a name from the list shown")


def return_book():
    user_return = input("Enter the name of book you want to return: ")
    if user_return in issued_books:
        books.append(user_return)
        issued_books.remove(user_return)
        print(user_return, 'returned')
    else:
        print(user_return,"was not issued")


    

def library():
    while True:
        print('\n_________________MENU_________________\n')
        print('1. Add Book')
        print('2. Show Books')
        print('3. Issue Books')
        print('4. Return Books')
        print('5. Exit')
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            show_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print('Aapke Baap ki dukan nhi hai. Paise de ke jana')
            break
        else:
            print('Invalid choice')


library()



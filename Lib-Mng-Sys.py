import mysql.connector as mys
mycon = mys.connect(host='localhost',user='root',password='sharma@1999')
mycur = mycon.cursor()


def search_book():
  a = input('Enter Book ID or Book Name : ')
  if a.isnumeric():
    query = "select * from books where id = {}".format(int(a))
  else :
    query = "select * from books where name = {}".format(a)
  mycur.execute(query)

def search_user():
  a = input('Enter User ID or User Name : ')
  if a.isnumeric():
    query = "select * from users where id = {}".format(int(a))
  else :
    query = "select * from users where name = {}".format(a)
  mycur.execute(query)

def issue_book():
  a = int(input('Enter Book ID : '))
  b = int(input('Enter User ID : '))
  query = "update books set issued_to = {} where id = {}".format(b,a)
  mycur.execute(query)
  query = "update users set book_assigned = {} where id = {}".format(a,b)
  mycur.execute(query)
  mycur.commit()

def return_book():
  a = int(input('Enter Book ID : '))
  query = "update books set issued_to = NULL where id = {}".format(a)
  mycur.execute(query)
  query = "update users set books_assigned = NULL where books_assigned = {}".format(a)
  mycur.execute(query)
  mycur.commit()

def update_books():
  print(
  '  [1] Add Books \n'
  '  [2] Delete Books \n'
  '  [3] Modify Details of Books')
  x = int(input('Enter Desired Number Option : '))
  if x == 1:
    print("Type 'EXIT' whenever you wish to exit the menu.")
    while True:
      i = input('Enter Book ID : ')
      if i.upper() == 'EXIT':
        break
      nm = input('Enter Book Name : ').upper()
      if nm.upper() == 'EXIT':
        break
      an = input('Enter Author Name : ').capitalize()
      if an.upper() == 'EXIT':
        break
     


print(
'Hey, What would you like to do?\n'
' [1] Search book from record\n'
' [2] Search user from record\n' 
' [3] Issue a Book\n'
' [4] Return a Book\n'
' [5] Update Inventory\n'
' [6] Update User Records\n'
)
n = int(input('Enter Desired Number Option: '))

while True:
  if n == 1:
    search_book()
  elif n == 2:
    search_user()
  elif n == 3:
    issue_book()
  elif n == 4:
    return_book()
  elif n == 5:
    update_books()
  elif n == 6:
    update_user()
  else:
    n = int(input('Please Enter a Valid Choice: '))
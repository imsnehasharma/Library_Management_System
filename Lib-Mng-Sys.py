import mysql.connector as mys
mycon = mys.connect(host='localhost',user='root',password='sharma@1999',database='Library_Management_System')
mycur = mycon.cursor()


def search_book():
  a = input('Enter Book ID or Book Name : ')
  if a == '*':
    query = "select * from books"
  elif a.isnumeric():
    query = "select * from books where id = {}".format(int(a))
  else :
    query = "select * from books where name = {}".format(a)
  mycur.execute(query)
  dt = mycur.fetchall()
  print('-'*80)
  print('%5s'%'ID', '%30s'%'Name', '%20s'%"Author's Name", '%20s'%'Issued To' )
  print('-'*80)
  for R in dt:
     print('%5s'%R[0], '%30s'%R[1], '%20s'%R[2], '%20s'%R[3])

def search_user():
  a = input('Enter User ID or User Name : ')
  if a == '*':
    query = "select * from users"
  elif a.isnumeric():
    query = "select * from users where id = {}".format(int(a))
  else :
    query = "select * from users where name = {}".format(a)
  mycur.execute(query)
  dt = mycur.fetchall()
  print('-'*80)
  print('%5s'%'ID', '%30s'%'Name', '%20s'%"Phone Number", '%20s'%'Books Borrowed' )
  print('-'*80)
  for R in dt:
     print('%5s'%R[0], '%30s'%R[1], '%20s'%R[2], '%20s'%R[3])


def issue_book():
  a = int(input('Enter Book ID : '))
  b = int(input('Enter User ID : '))
  query = "select issued_to from books"
  mycur.execute(query)
  dt = mycur.fetchone()
  if dt==():
    query = "update books set issued_to = {} where id = {}".format(b,a)
    mycur.execute(query)
    query = "update users set books_assigned = {} where id = {}".format(a,b)
    mycur.execute(query)
    mycon.commit()
    query = "select books.name, users.name from books, users where books.issued_to = users.id"
    mycur.execute(query)
    dt = mycur.fetchone()
    print(dt[0],'is Issued to',dt[1])
  else:
    print('Sorry, but the Book is unavailable.')

def return_book():
  a = int(input('Enter Book ID : '))
  query = "update books set issued_to = NULL where id = {}".format(a)
  mycur.execute(query)
  query = "update users set books_assigned = NULL where books_assigned = {}".format(a)
  mycur.execute(query)
  mycon.commit()
  print('The Book is Returned.')

def update_books():
  print(
  '  [1] Add Books \n'
  '  [2] Delete Books \n'
  '  [3] Modify Details of Books')
  x = int(input('Enter Desired Number Option : '))
  if x == 1:
    print("Type 'EXIT' whenever you wish to exit the menu.")
    while True:
      nm = input('Enter Book Name : ').upper()
      if nm.upper() == 'EXIT':
        break
      an = input('Enter Author Name : ').capitalize()
      if an.upper() == 'EXIT':
        break
      query = "insert into books (name,author_name) values('{}','{}')".format(nm,an)
      mycur.execute(query)
      mycon.commit()
      query = "select * from books"
      mycur.execute(query)
      dt = mycur.fetchall()
      print('-'*80)
      print('%5s'%'ID', '%30s'%'Name', '%20s'%"Author's Name", '%20s'%'Issued To' )
      print('-'*80)
      for R in dt:
        print('%5s'%R[0], '%30s'%R[1], '%20s'%R[2], '%20s'%R[3])
 
     


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
    break
  elif n == 2:
    search_user()
    break
  elif n == 3:
    issue_book()
    break
  elif n == 4:
    return_book()
    break
  elif n == 5:
    update_books()
  elif n == 6:
    update_user()
  else:
    n = int(input('Please Enter a Valid Choice: '))
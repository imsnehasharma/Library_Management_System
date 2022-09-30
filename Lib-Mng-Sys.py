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
 
def add_books():
  query = "select Max(id) from books"
  mycur.execute(query)
  dt = mycur.fetchone()
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
  query = "select * from books where id > {}".format(dt[0])
  mycur.execute(query)
  dt = mycur.fetchall()
  print('Following Books have been added')
  print('-'*80)
  print('%5s'%'ID', '%30s'%'Name', '%20s'%"Author's Name", '%20s'%'Issued To' )
  print('-'*80)
  for R in dt:
    print('%5s'%R[0], '%30s'%R[1], '%20s'%R[2], '%20s'%R[3])
def del_books():
  while True:
    a = input('Enter ID of the Book to be Deleted : ')
    if a.upper() == 'EXIT':
      break
    else:
      query = "delete from books where id = {}".format(int(a))
      mycur.execute(query)
      mycon.commit()
      print('Book of the Given ID has been removed from Inventory.')
def mod_books():
  while True:
    a = int(input('Enter Book ID : '))
    if a.upper() == 'EXIT':
      break
    else:
      b = int(input('What would you like to change? \n'
      '   [1] Book Name \n'
      '   [2] Author Name \n'))
      while True:
        if b == 1:
          nm = input('Enter New Name : ')
          query = "update books set name = '{}' where id = {}".format(nm,a)
          break
        elif b == 2:
          an = input('Enter New Author Name : ')
          query = "update books set author_name = '{}' where id = {}".format(an,a)
          break
        else :
          b = int(input('Please Enter a Valid Choice : '))
      mycur.execute(query)
      mycon.commit()
      query = "select * from books where id = {}".format(a)
      mycur.execute(query)
      dt = mycur.fetchone()
      print('Changes have been made')
      print('-'*80)
      print('%5s'%'ID', '%30s'%'Name', '%20s'%"Author's Name", '%20s'%'Issued To' )
      print('-'*80)
      print('%5s'%dt[0], '%30s'%dt[1], '%20s'%dt[2], '%20s'%dt[3])

def update_books():
  print(
  '  [1] Add Books \n'
  '  [2] Delete Books \n'
  '  [3] Modify Details of Books')
  x = int(input('Enter Desired Number Option : '))

  print("Type 'EXIT' whenever you wish to exit the menu.")

  if x == 1:
    add_books()
  elif x == 2:
    del_books()
  elif x == 3:
    mod_books()

def add_users():
  query = "select Max(id) from users"
  mycur.execute(query)
  dt = mycur.fetchone()
  while True:
    nm = input('Enter User Name : ').caitalize()
    if nm.upper() == 'EXIT':
      break
    pn = input('Enter Phone Number : ')
    if pn.upper() == 'EXIT':
      break
    query = "insert into users (name,phone_no) values('{}','{}')".format(nm,pn)
    mycur.execute(query)
    mycon.commit()
  query = "select * from users where id > {}".format(dt[0])
  mycur.execute(query)
  dt = mycur.fetchall()
  print('Following Users have been added')
  print('-'*80)
  print('%5s'%'ID', '%30s'%'Name', '%20s'%"Phone Number", '%20s'%'Books Borrowed' )
  print('-'*80)
  for R in dt:
     print('%5s'%R[0], '%30s'%R[1], '%20s'%R[2], '%20s'%R[3])
def del_users():
  while True:
    a = input('Enter ID of the User to be Deleted : ')
    if a.upper() == 'EXIT':
      break
    else:
      query = "delete from users where id = {}".format(int(a))
      mycur.execute(query)
      mycon.commit()
      print('User of the Given ID has been removed from the User List.')
def mod_users():
  while True:
    a = int(input('Enter User ID : '))
    if a.upper() == 'EXIT':
      break
    else:
      b = int(input('What would you like to change? \n'
      '   [1] Name \n'
      '   [2] Phone Number \n'))
      while True:
        if b == 1:
          nm = input('Enter New Name : ')
          query = "update users set name = '{}' where id = {}".format(nm,a)
          break
        elif b == 2:
          an = input('Enter New Phone Number : ')
          query = "update users set phone_no = '{}' where id = {}".format(an,a)
          break
        else :
          b = int(input('Please Enter a Valid Choice : '))
      mycur.execute(query)
      mycon.commit()
      query = "select * from users where id = {}".format(a)
      mycur.execute(query)
      dt = mycur.fetchone()
      print('-'*80)
      print('%5s'%'ID', '%30s'%'Name', '%20s'%"Phone Number", '%20s'%'Books Borrowed' )
      print('-'*80)
      print('%5s'%dt[0], '%30s'%dt[1], '%20s'%dt[2], '%20s'%dt[3])

def update_user():
  print(
  '  [1] Add User \n'
  '  [2] Delete User \n'
  '  [3] Modify Details of User')
  x = int(input('Enter Desired Number Option : '))

  print("Type 'EXIT' whenever you wish to exit the menu.")

  if x == 1:
    add_users()
  elif x == 2:
    del_users()
  elif x == 3:
    mod_users()

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
    print('='*100)
    search_book()
    print('='*100)
    break
  elif n == 2:
    print('='*100)
    search_user()
    print('='*100)
    break
  elif n == 3:
    print('='*100)
    issue_book()
    print('='*100)
    break
  elif n == 4:
    print('='*100)
    return_book()
    print('='*100)
    break
  elif n == 5:
    print('='*100)
    update_books()
    print('='*100)
    break
  elif n == 6:
    print('='*100)
    update_user()
    print('='*100)
    break
  else:
    n = int(input('Please Enter a Valid Choice: '))
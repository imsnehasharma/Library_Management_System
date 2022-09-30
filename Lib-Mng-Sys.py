#import mysql.connector as mys
#mycon = mys.connect(host='localhost',user='root',password='lms')
#mycur = mycon.cursor()


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
  query = "update books set issued_to = {}".format(b)
  mycur.execute(query)
  query = "update users set book_assigned = {}".format(a)






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
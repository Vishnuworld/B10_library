from book.models import Book
from django.contrib.auth.models import User

# User.objects.create_user(username="Mayuri", email="mayuri@gmail.com", password="Python@123")
# User.objects.create_superuser(username="Monal", email="monal@gmail.com", password="Python@123")
# obj = User.objects.get()

# print(User.objects.all())

# exec(open(r'E:\Python-B10\Files\Django_Projects\LibraryProject\book\db_shell.py').read())

# Book.objects.filter(isdeleted=True)  # in-active
# Book.objects.filter(isdeleted=False)  # active

# print(Book.objects.get_active_objects())
# print(Book.objects.get_inactive_objects())
# print(Book.objects.all())
from datetime import datetime

Book.objects.using("secondary").create(title="Book5", author="Auth5", 
                    publication_date=datetime(2023, 10, 25), price=578)

# middleware -- 

# session data --- server side
# cookies -- client side


# form
# file save  --->
# custom command
# inspectdb
# login logout --



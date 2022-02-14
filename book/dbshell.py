from django.contrib.auth.models import User

# exec(open(r"D:\ViRaj's\Work\Data Science\VSC Projects\Django\Library\book\dbshell.py").read())

User.objects.create(username="abcd", password="1234")           # stores password as it is
User.objects.create_user(username="xyz", password="0987")       # stores password in encrypted format


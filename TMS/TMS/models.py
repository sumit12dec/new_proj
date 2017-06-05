from django.db import models

class UserModel(models.Model):
	# user_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	role = models.CharField(max_length=100, choices=(
			('admin', 'admin'),
			('regular', 'regular'),
				))
	date_joined = models.DateTimeField(auto_now_add=True)
from django.db import models

# Create your models here.
class Keyword(models.Model):
    keyword = models.CharField(max_length=50)   # keyword is the search string entered by the user


class User(models.Model):
    user_id = models.IntegerField(unique= True)   # user_id is the unique identifier for the user's github profile
    username = models.CharField(max_length=50)
    profile_url = models.CharField(max_length=200)
    email = models.EmailField(max_length=60,null= True) # null=True allows for blank email user may not have a publicly available email
    name = models.CharField(max_length=50) 
    bio = models.TextField(max_length=500,null=True) # null=True allows for blank bio user may not have a publicly available bio
    query_id = models.ForeignKey(Keyword, verbose_name=("The related query for this user"), on_delete=models.CASCADE)
    twitter_url = models.CharField(max_length=200,null=True)
    location = models.CharField(max_length=50,null=True)
    avatar_url = models.CharField(max_length=200,null=True)
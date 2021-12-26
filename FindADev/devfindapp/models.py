from django.db import models

# Create your models here.
class Keyword(models.Model):
    keyword = models.CharField(max_length=50)   # keyword is the search string entered by the user


class User(models.Model):
    user_id = models.IntegerField(unique= True)   # user_id is the unique identifier for the user's github profile                      # JSON->  id
    username = models.CharField(max_length=50)  # username is the user's github username                                                # JSON->  login
    profile_url = models.CharField(max_length=200) # profile_url is the user's github profile url                                       # JSON->  html_url   
    email = models.EmailField(max_length=60,null= True) # null=True allows for blank email user may not have a publicly available email # JSON->  email
    name = models.CharField(max_length=50)  # name is the user's full name                                                              # JSON->  name
    bio = models.TextField(max_length=500,null=True) # null=True allows for blank bio user may not have a publicly available bio        # JSON->  bio
    query_id = models.ForeignKey(Keyword, verbose_name=("The related query for this user"), on_delete=models.CASCADE) # query_id is the id of the query that generated this user
    twitter_url = models.CharField(max_length=200,null=True) # twitter_url is the user's twitter profile url                            # JSON->  twitter_username
    location = models.CharField(max_length=50,null=True) # location is the user's location                                              # JSON->  location
    avatar_url = models.CharField(max_length=200,null=True) # avatar_url is the user's avatar url                                       # JSON->  avatar_url
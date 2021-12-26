import requests
from django.shortcuts import render

# Create your views here.
SEARCH_URL = 'https://api.github.com/search/users?q=language:python' # My plan is, basically search the users by the appropriate language, and then display the results.
 
def search(request):

  params = {
      "Authorization": 'token ' + GITHUB_AUTH_TOKEN,
      'accept': 'application/vnd.github.v3+json',# adding this header to the GET request is recommended by the API documentation 
      'per_page': '1',
        'page': '1',
  }
  user_list = requests.get(SEARCH_URL, params=params); # this request returns a list of users, which we can then iterate through to display the results.
  iuser_list = user_list.json()
  usrs_urls = [] # will store relevant profile urls for each user, this urls are another API endpoints, which we can use to get the user's profile information.
  for user in iuser_list['items']:
    usrs_urls.append(user['url'])
  users = []

# get relevant user information from each user's profile url
  for url in usrs_urls:
    user_info = requests.get(url, params=params)
    user_info = user_info.json()
    users.append(user_info)

  print(users[0])
  ans = requests.get('https://api.github.com/rate_limit')
  print (ans.json()['resources']['core']['remaining'])
  print (ans.json()['resources']['search']['remaining'])
 # for user in users:
 #   print('*'*50)
 #   print(user['name'])
 #   print(user['id'])
 #   print(user['login'])
 #   print(user['email'])
 #   print(user['twitter_username'])
 #   print(user['html_url'])
 #   print(user['avatar_url'])
 #   print(user['bio'])
 #   print(user['location'])
  return render(request, 'search/index.html')


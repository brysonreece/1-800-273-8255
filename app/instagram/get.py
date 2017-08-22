import httplib, json, urllib, base64
from array import *

def search_user(username):
  conn = httplib.HTTPSConnection('www.instagram.com')
  conn.request("GET", "/" + username + "/?__a=1")
  response = conn.getresponse()
  data = response.read()
  json_data = json.loads(data)
  return json_data

def get_pictures(username):
  json_data = search_user(username)
  urls = []
  nodes = json_data["user"]["media"]["nodes"]
  for node in nodes:
    url = node["display_src"]
    urls.append(url)

  return urls

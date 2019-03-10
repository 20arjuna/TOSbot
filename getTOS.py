# from googlesearch import search
# print('running')
# query = "google.com privacy policy"
# resultList = []
# print('entering loop now!')
# for j in search(query, tld="co.in", num=10, stop=1, pause=2):
#     resultList.append(j)
#     print(j)
import requests
from bs4 import BeautifulSoup

text = "google privacy policy"
url = "https://www.google.com/search?q=" + text

response = requests.get(url)
print(response)
# soup = BeautifulSoup(response.text,"lxml")
# for item in soup.select(".r a"):
#     f_url = item.get('href')
#     myurl = f_url.replace(f_url[:7], '')
#     myurl = myurl.split('&')
#     myurl = myurl[0]
#     print(myurl)
#     break
#
# print ('Searching from:\n' + myurl)
# f_response = requests.get(myurl)
# f_soup = BeautifulSoup(f_response.text,"lxml")
#
# print (f_soup.get_text())

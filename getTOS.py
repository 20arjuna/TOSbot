from googlesearch import search
print('running')
query = "google.com privacy policy"
resultList = []
print('entering loop now!')
for url in search('redis terms of service', tld='com', lang='en', stop=5):
    print(url)

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

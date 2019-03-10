from googlesearch import search
print('running')
query = "mail.google.com privacy policy"

print('entering loop now!')

if((query.__contains__('google')) or (query.__contains__('youtube')) or (query.__contains__('gmail'))):
    privacy_policy = "https://policies.google.com/privacy?hl=en"
else:
    for url in search(query, tld='com', lang='en', stop=1):
        privacy_policy=url
print(privacy_policy)

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

from flask import Flask,render_template, Response, request, redirect, url_for, send_file
import json
app = Flask(__name__)


@app.route("/")

def hello():
    return render_template('loading.html')
@app.route('/getPrivacyUrl', methods=['POST'])
def getPrivacyUrl():
    j = json.loads(request.data.decode())
    sitename = j.get("sitename")

    from googlesearch import search
    print('running')
    query = sitename + " privacy policy"

    print('entering loop now!')

    if((query.__contains__('google')) or (query.__contains__('youtube')) or (query.__contains__('gmail'))):
        privacy_policy = "https://policies.google.com/privacy?hl=en"
    else:
        for url in search(query, tld='com', lang='en', stop=1):
            privacy_policy=url
    print(privacy_policy)
    return(privacy_policy)
if __name__ == "__main__":
    app.run()


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

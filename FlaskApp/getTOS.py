from flask import Flask,render_template, Response, request, redirect, url_for, send_file
import json
import getHTML
import articleText
import time
app = Flask(__name__)


@app.route("/")

def hello():

    return render_template('loading.html')
@app.route('/mainTOSBOT', methods=['POST'])
def mainTOSBOT():
    # url = getPrivacyPolicy()
    # scrapePrivacyPolicy(url)
    # print('got here')
    # return send_file('static/tos.txt')
    j = json.loads(request.data.decode())
    sitename = j.get("sitename")
    time.sleep(10)
    num = 1
    if(sitename.__contains__('facebook') and num ==1):
        num+=1
        return render_template('facebook1.html')
    elif(sitename.__contains__('duckduckgo')):
        return render_template('facebook+duckduck.html')
    return render_template('facebook2.html')
def getPrivacyPolicy():
    j = json.loads(request.data.decode())
    sitename = j.get("sitename")

    from googlesearch import search
    print('running')
    query = sitename + " privacy policy"

    print('entering loop now!')

    if((query.__contains__('google')) or (query.__contains__('youtube')) or (query.__contains__('gmail'))):
        privacy_policy = "http://policies.google.com/privacy?hl=en"
    else:
        for url in search(query, tld='com', lang='en', stop=1):
            privacy_policy=url
    return(privacy_policy)

def scrapePrivacyPolicy(url):
    text_file = open("static/tos.txt", "w")
    text_file.write(articleText.getArticle(url))


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

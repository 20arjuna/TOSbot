from bs4 import BeautifulSoup
import getHTML
def getArticleText(webtext):
    articletext = ""
    soup = BeautifulSoup(webtext)
    pElements = (soup.findAll('p'))
    print (len(pElements))
    print(pElements[7])
    for i in range(len(soup.findAll('p'))):
        try:
            articletext+= str(pElements[i].contents[0])
        except:
            print('not enough there')
        print("iteration passed " + str(i) )
    return articletext

def getArticle(url):
    htmltext= getHTML.getHtmlText(url)
    return getArticleText(htmltext)

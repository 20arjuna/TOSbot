from bs4 import BeautifulSoup
import getHTML
def getArticleText(webtext):
    articletext = ""
    soup = BeautifulSoup(webtext)
    for tag in soup.findAll('p'):
        articletext+= tag.contents[0]
    return articletext

def getArticle(url):
    htmltext= getHTML.getHtmlText(url)
    return getArticleText(htmltext)

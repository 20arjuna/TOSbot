import mechanize
def scrapePrivacyPolicy(url):
    br = mechanize.Browser()
    htmltext = br.open(getPrivacyUrl())
    return htmltext

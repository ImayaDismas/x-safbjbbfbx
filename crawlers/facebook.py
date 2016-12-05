import urllib2  #will need to port this to python3
import urllib   #will need to port this to python3
import cookielib
import sys
import json
import re
import time
from lxml import html as htmlParser
from bs4 import BeautifulSoup, Comment
import os
import cPickle as pickle
#variables

   #facebook

login_url = 'http://m.facebook.com/login.php?m=m&refsrc=m.facebook.com%2F'
search_url = 'https://www.facebook.com/search/top/?q='
email = '254nostra@gmail.com'
pwd = 'synergetic'
facebook_test_no = '0728117996'
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0'
cookie_file = open('cookies.txt','w')
cookie_file.close
cj = cookielib.LWPCookieJar('cookies.txt') #cookiejar
counter = 0

searchresults = []
valid = ""
searchterm = {"term":"", "type":""}


    #truecaller
APIToken = "sl9KG2Yh4b"
truecaller_test_no = "254726090246" # Test Number
truecaller_search_url = "https://tcapi.phphive.info/"
request_headers = {
"X-User": "PHPHive"
}



pickle_filepath = "time.pickle"



def truecallerSearch(term):
    """
    """
    print "Searching for "+term;
    request = urllib2.Request(truecaller_search_url+APIToken+"/search/"+term, headers=request_headers)
    contents = urllib2.urlopen(request).read()
    print contents

def facebook_log_in():
    """
    this function logs us into facebook as nostra
    and returns a cookie that we can use for searching
    """
    #login and set cookie
    params = urllib.urlencode({'email':email,'pass':pwd,'login':'Log+In'})
    login_req = urllib2.Request(login_url, params)
    #login_req.add_header('User-Agent':user_agent)
    login_response = urllib2.urlopen(login_req)
    #save cookie to file
    cj.save()


def facebookSearch(term):
    """
    This function somehow checks if we are already logged into facebook
    If not then we can log in. This allows us to reuse a session
    We check by trying a search. If we get a 'No results for your query' response, we are not logged in,
    We then try to log in a maximum of 3 times. If the search is successful
    we proceed to parsing the search response
    """
    #configure the facebook opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    try:
        cj.load() #Trying to load the cookie file
        print("cookie load successful")
    except IOError: #catch IO error
        print "Loading stored cookies failed..."
    global counter

    #search request

    print("searching "+term['term'])
    search_req = urllib2.Request(search_url+term['term'])
    #req2.add_header('User-Agent': user_agent)
    search_response = urllib2.urlopen(search_req)
    print("got a response")
    html = search_response.read()
    data = search_response.info()
    #write html to file
    target = open((term['term']+'.html'), 'w')
    target.truncate()
    target.write(html)
    target.close

    htmlObj = htmlParser.parse(term['term']+'.html')
    if not facebook_logged_in(htmlObj):
        if counter<3:
            print("trying to log in attempt "+(counter-1))
            counter = counter + 1
            facebook_log_in()
            search()  #recursively try to search
    elif counter>3:
        counter = 0
        print("time out")
        print("login failed...please reconfigure")
    elif nosearchresult(htmlObj,term['term']):
        print("No search results for " + term['term'])
    else:
        print("Gotcha!!")
        counter = 0
        extract(htmlObj,term)



def extract(htmlObj,term):

    """
    for event, element in etree.iterparse(html,events=("start", "end")):
        if element.tag in ['div','img']:
            print("%5s, %4s, %s , %s" % (event, element.tag, element.text, element.tail))
    """
    print("searching for content column")
    resultdivs = htmlObj.findall(".//code")

    cleansoups = []
    for div in resultdivs:
        string =htmlParser.tostring(div)
        soup = BeautifulSoup(string,'lxml')
        comment= soup.findAll(text = lambda text:isinstance(text,Comment))
        if len(comment)>0:
            comment[0].strip()
            cleansoup = BeautifulSoup(comment[0],'lxml')
            if cleansoup.find("div",{"class":"_glj"}):
                print "content"
                cleansoups.append(cleansoup)
        else:
            print "None"
    if len(cleansoups) ==1:
        buttons = cleansoups[0].findAll("div",{"class":"FriendButton"})
        if buttons:
            for button in buttons:
                button.clear()
        others = cleansoups[0].findAll("span")
        if others:
            for other in others:
                other.clear()
        footers = cleansoups[0].findAll("footer")
        if footers:
            for footer in footers:
                footer.clear()
        html = cleansoups[0].prettify("utf-8")
        with open(term['term']+".html", "wb") as file:
            file.truncate()
            file.write(html)
        imagetag = cleansoups[0].findAll("img")[0]
        edu_workdivs = cleansoups[0].findAll("div",{"class":"_52eh"})
        edu = ""
        work = ""
        edulink = ""
        worklink = ""
        for edu_workdiv in edu_workdivs:
            if "Alisomea" in edu_workdiv.text or "Alisoma katika" in edu_workdiv.text or "katika" in edu_workdiv.text:
                edu = edu_workdiv.a.text
                edulink = edu_workdiv.a['href']
            elif edu_workdiv.a is not None:
                work = edu_workdiv.a.text
                worklink = edu_workdiv.a['href']
        name = cleansoups[0].findAll("div",{"class":"_5d-5"})[0].text
        if term['type'] == 'phone':
            phone = term['term']
            email = ""
        else:
            email = term['term']
            phone = ""

        print (imagetag.prettify("utf-8"))
        print name
        print edu
        print edulink
        print worklink
        print work



        searchresults.append({"term":term['term'],"name":name, "number":phone, "email":email, "edu":{"place":edu, "link":edulink},"work":{"place":work, "link":worklink},"imagesrc":imagetag['src']})


        with open(term['term']+'.json', 'w') as outfile:
            json.dump(searchresults, outfile)

    #print (contentCol.text_content())
def facebook_logged_in(htmlObj):
    noresultdivs = htmlObj.findall(".//div[@id='pagelet_search_no_results']")
    #noresultdivString = html.tostring(noresultdiv)
    #soup = BeautifulSoup(noresultString,'lxml')
    if len(noresultdivs) ==0:
        return True

    return False


def nosearchresult(htmlObj,term):
    codedivs = htmlObj.findall(".//code")
    print (len(codedivs))
    for codediv in codedivs:
        nostring =htmlParser.tostring(codediv)
        nosoup = BeautifulSoup(nostring,'lxml')
        nocomment= nosoup.findAll(text = lambda text:isinstance(text,Comment))
        if nocomment is not None and len(nocomment)>0:
            nocomment[0].strip()
            hiddendiv = BeautifulSoup(nocomment[0],'lxml')

            if hiddendiv.find_all("div",{"id":"pagelet_search_no_results"}):
                #print(hiddendiv.prettify)
                return True
    return False

def getquery():
    global valid
    query_term = raw_input("Please enter a"+valid+" search term: ")
    verifyinput(query_term)

def verifyinput(query_term):
    if not re.match(r'[^@]+@[^@]+\.[^@]+', query_term):
        if not re.match(r'(\+){0,1}([0-9]){5,12}',query_term):
            valid = "valid"
            getquery()
        else:
            searchterm['term'] = query_term
            searchterm['type'] = 'phone'
    else:
        searchterm['term'] = query_term
        searchterm['type'] = 'email'

if __name__ == "__main__":
    facebook_log_in()
    if len(sys.argv) == 2:
        raw_term = sys.argv[1]
        verifyinput(raw_term)
    else:
        getquery()
    facebookSearch(searchterm)
    if searchterm['type'] == 'phone':
        now = time.time()
        if not os.path.exists(pickle_filepath):
            # Read data set from disk
            with open(pickle_filepath, 'w') as pickle_handle:
                pickle.dump(now, pickle_handle)
                truecallerSearch(searchterm['term'])
        else:
            with open(pickle_filepath) as pickle_handle:
                before = pickle.load(pickle_handle)
            with open(pickle_filepath, 'w') as pickle_handle:
                pickle.dump(now, pickle_handle)
            interval = int(now - before)
            if interval < 60:
                print "Wait for"+str(65-interval)+ " seconds!!"
                time.sleep(65 - interval)
                print "searching"
            truecallerSearch(searchterm['term'])

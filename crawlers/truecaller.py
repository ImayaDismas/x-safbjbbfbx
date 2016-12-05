import urllib2

APIToken = "sl9KG2Yh4b"
no = "0700415505" # Any Number You Want to Search

request_headers = {
"X-User": "PHPHive"
}

# For Searching User Details
print "Searching for "+no;
request = urllib2.Request("https://tcapi.phphive.info/"+APIToken+"/search/"+no, headers=request_headers)
contents = urllib2.urlopen(request).read()
print contents

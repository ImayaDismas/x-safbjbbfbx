#!C:\Python27\python.exe -u
#!/usr/bin/env python
  
import cgi
   
print "Content-type: text/html"
print
   
print """
<html>
  
<head><title>Sample CGI Script</title></head>
  
<body>
   
<h3> Sample CGI Script </h3>
"""
  
 
  
print """
  
</body>
</html>
""" % cgi.escape(message)

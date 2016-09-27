import web
import json,urllib
 
def make_text(string):
    return string

#this is the string to encode
json_string = '{ "number": "9999999999", "name": "Salman Khan", "gender": "Male", "spamScore": 3372, "spamType": "TOP_SPAMMER", "address": null, "email": null, "facebook": null, "twitter": null, "image": null, "tags": "Finance, Insurance & Legal,Bank," }'
#this can print the entire string
#print(json.dumps(json_string))

#encoding the string
parsed_json = json.loads(json_string)

#Own json to try
data = urllib.urlopen("templates/data.json").read()
output = json.loads(data)
print (output)
    
#end of json trial


 
urls = ('/', 'tutorial')
render = web.template.render('templates/')
 
app = web.application(urls, globals())
 
my_form = web.form.Form(
                web.form.Textbox('', class_='name', id='name'),
                )
 
class tutorial:
    def GET(self):
        form = my_form()
        return render.tutorial(form, "Your text goes here.")
         
    def POST(self):
        form = my_form()
        form.validates()
        print("I am Here 0")
        for user in  parsed_json.items():
            print("I am Here 1")
            if form.value['name'] in user:
                print("I am Here 2")
                name = parsed_json['name']
                number = parsed_json['number']
                gender = parsed_json['gender']
                array = []
                print(make_text(name))
                array.append(make_text(name))
                print(make_text(number))
                array.append(make_text(number))
                print(make_text(gender))
                array.append(make_text(gender))
                return array
    
#        s = form.value['name'] +" "+ parsed_json['number']
#        return make_text(s)
    
if __name__ == '__main__':
    app.run()

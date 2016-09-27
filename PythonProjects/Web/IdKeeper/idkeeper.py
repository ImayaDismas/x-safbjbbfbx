import json

#this is the string to encode
json_string = '{ "number": "9999999999", "name": "Salman Khan", "gender": null, "spamScore": 3372, "spamType": "TOP_SPAMMER", "address": null, "email": null, "facebook": null, "twitter": null, "image": null, "tags": "Finance, Insurance & Legal,Bank," }'

#this can print the entire string
#print(json.dumps(json_string))

#encoding the string
parsed_json = json.loads(json_string)

#accessing individual items
print(parsed_json['number'])
print(parsed_json['name'])
print(parsed_json['email'])
print(parsed_json['facebook'])
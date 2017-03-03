# !/usr/bin/python3

import os
import json

directory_list = list()
for root, dirs, files in os.walk("/home/.exploits", topdown=False):
    for name in dirs:
        directory_list.append(os.path.join(root, name))

print (directory_list)
print(json.dumps(directory_list))
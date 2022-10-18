#JSON, JavaScript Object Notation, which is technically related to yet another
#programing language called JavaScript. but JSON itself is typically used
#nowadays as a language agnostic format for exchanging data between computers.

import json
import requests
import sys

#get value from command line
if len(sys.argv) == 2:
    pass


response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# print(json.dumps(response.json(), indent=2))

o = response.json()

print(o)
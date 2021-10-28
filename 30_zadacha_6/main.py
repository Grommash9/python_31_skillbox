import requests
import re

results = requests.get('http://www.columbia.edu/~fdc/sample.html')

example_good_number = r'[<h3 id=]{7}(.{0,900})[</h3>]{5}'

list_h3 = re.findall(example_good_number, results.text)

for h3_tags_data in list_h3:
    print(h3_tags_data)


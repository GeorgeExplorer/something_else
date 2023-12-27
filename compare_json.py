"""'
Comparing 2 json files to detect any differences
'"""

# import library to work with json files
import json

# open first file and read the data
with open('/Users/geotestertestov/Downloads/response_1.json', 'r') as r_1:
    data_1 = json.load(r_1)
# print(data_1)

# open second file and read the data
with open('/Users/geotestertestov/Downloads/response_2.json', 'r') as r_2:
    data_2 = json.load(r_2)
print(data_2)

# write each objectid of 1st json file into list_1
objectid_list_1 = [i["objectid"] for i in data_1['data']]

# write each objectid of 2nd json file into list_2
object_id_list_2 = [i["object_id"] for i in data_2['results']]

# start comparing two files
if set(objectid_list_1) == set(object_id_list_2):
    print('Everything is the same')
else:
    print('There\'re some differences')
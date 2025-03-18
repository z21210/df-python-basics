import csv
import json
from pathlib import Path

TRAINER_DEMO_FILES = 'demo_files'

current_dir = Path.cwd()

FILE_NAME = [
    'data.csv',
    'new_data.csv',
    'data.tsv',
    'new_data.tsv',
    'new_data.json'
]

demo_csv_file_path = current_dir / TRAINER_DEMO_FILES / FILE_NAME[0]

# with open(demo_csv_file_path) as csv_file:
#     read_csv = csv.reader(csv_file)
#     # print(read_csv)
#     for row in read_csv:
#         print(row)
#         for cell in row:
#             print(cell)

# Create our own CSV file
data = [
    ['Name', 'Age'],
    ['Alice', 24],
    ['Bob', 32]
]

new_file_path = current_dir / TRAINER_DEMO_FILES / FILE_NAME[1]

with open(new_file_path, mode="w") as new_csv_file:
    new_data = csv.writer(new_csv_file)
    new_data.writerows(data)

with open(new_file_path) as new_csv:
    read_data = csv.reader(new_csv)
    for row in read_data:
        print(row)

'''
TSV FILES
'''

tsv_file_path = current_dir / TRAINER_DEMO_FILES / FILE_NAME[2]

with open(tsv_file_path) as tsv_file:
    tsv_data = csv.reader(tsv_file, delimiter='\t')
    for row in tsv_data:
        print(row)

new_tsv_file_path = current_dir / TRAINER_DEMO_FILES / FILE_NAME[3]

with open(new_tsv_file_path, mode='w') as new_tsv:
    new_data = csv.writer(new_tsv, delimiter='\t')
    new_data.writerows(data)

json_data = [
    {
        'name': 'Alice',
        'age': 24,
        'address': {
            'street': '123 Fake St',
            'city': 'Springfield'
        }
    },
    {
        'name': 'Bob',
        'age': 32,
        'address': {
            'street': '125 Fake St',
            'city': 'Springfield'
        }
    },
]

new_json_file_path = current_dir / TRAINER_DEMO_FILES / FILE_NAME[4]

with open(new_json_file_path, mode='w') as json_file:
    data = json.dump(json_data, json_file)

with open(new_json_file_path) as read_json:
    data = json.load(read_json)
    print(data)
    print(type(data))

# homework 15 - Converting JSON to CSV-file
import csv
import json
import time

from pathlib import Path

input_dir = Path('./input_files')
input_dir.mkdir(exist_ok=True)
print(f'For start reading please copy JSON-file \'people_db.json\' to this directory: {input_dir.absolute()}')

output_dir = Path('./output_files')
output_dir.mkdir(exist_ok=True)
print(f'Your CSV-file will be created into directory: {input_dir.absolute()}')

time.sleep(15)
next_step = input('To continue press \'Y\': ')
if next_step.upper() == 'Y':
    print('Starts the process of reading JSON-file and writing CSV-file')

    json_input_file = Path.joinpath(input_dir, 'people_db.json')
    csv_output_file = Path.joinpath(output_dir, 'filtered_people.csv')

    if json_input_file.exists():
        people_data = []
        count = 0

        # reading from JSON-file
        with open(json_input_file) as json_file:
            json_data = json.load(json_file)
            for num, people in enumerate(json_data):
                if people['company_name'] is None and people['phone'] is not None \
                        and people.get('job_title').lower().find('software') != -1:
                    count += 1
                    people_data.append(people)

        # field names
        # fields = ['first_name', 'last_name', 'email_address', 'company_name', 'job_title', 'phone']
        fields = []
        for key in people_data[0]:
            fields.append(key)

        # writing to csv file
        with open(csv_output_file, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields, dialect='excel', delimiter=';')
            writer.writeheader()
            writer.writerows(people_data)

        print(f'{count} items were written to CSV-file')

    else:
        print(f'{json_input_file} doesn\'t exists')
else:
    print('Refusal to read the file')

print('Done!')

import json
import csv

f = open('annotations v1.0.json', encoding="utf8")

annotations = json.load(f)
final_data = [[["Sentence #"], ["Word"], ["Tag"]]]

#for i in annotations['emp_details']:
#    print(i)

#print(annotations['classes'])

for sentence_no, item in enumerate(annotations['annotations']):
    tokens = item[0].split()
    for token in tokens:
        row = []
        row.append([sentence_no + 1])
        row.append([token])

        for entity in item[1]["entities"]:
            extracted = item[0][entity[0] : entity[1]]
            if token == extracted:
                row.append([entity[2]])

        if len(row) == 2:
            row.append(["OTHER"])

        final_data.append(row)

print(final_data)

with open('ner_dataset3.csv', 'w', encoding="utf8") as file:
    writer = csv.writer(file)
    writer.writerow(final_data)

# Closing file
f.close()
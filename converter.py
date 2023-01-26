import json
import csv

f = open('annotations v1.3.json', encoding="utf8")

annotations = json.load(f)
# final_data = [["Sentence #", "Word", "Tag"]]

# for i in annotations['emp_details']:
#    print(i)

#print(annotations['classes'])

with open('ner_dataset1.3.csv', 'w', newline='', encoding="utf8") as file:
    writer = csv.writer(file)
    writer.writerow(["Sentence #", "Word", "Tag"])

    for sentence_no, item in enumerate(annotations['annotations']):
        tokens = item[0].split()
        for token in tokens:
            row = []
            row.append(sentence_no + 1)
            row.append(token)

            for entity in item[1]["entities"]:
                sentence = item[0]
                start_char = entity[0]
                end_char = entity[1]
                extracted = sentence[start_char: end_char]

                if token == extracted or token in extracted:
                    if len(row) == 2:
                        row.append(entity[2])

            if len(row) == 2:
                row.append("OTHER")

            writer.writerow(row)

# Closing file
# f.close()
import json
with open('train_data/invoice (2).json', 'r', encoding='utf-8') as fp:
    labels = json.load(fp)

print(labels)
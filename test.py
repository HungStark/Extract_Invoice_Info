import json
import simplejson
with open('train_data/invoice (2).json', 'r', encoding='utf-8') as fp:
    labels = simplejson.loads(fp.read())

with open('invoice (2).json', 'w', encoding='utf-8') as fp:
    fp.write(simplejson.dumps(labels, indent=2, ensure_ascii=False))
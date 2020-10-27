# sort Actions in AWS policy json

import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('cs_policy.json') as json_file:
    data = json.load(json_file)
    for key, value in data.items():
        if key == 'Statement':
            # print(value[0])
            for k, v in value[0].items():
                if k == "Action":
                    v.sort()
                    # pp.pprint(v)

with open('cs_policy_sorted.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

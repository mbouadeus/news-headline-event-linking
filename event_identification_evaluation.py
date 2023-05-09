import os
import json
import csv

linking_outputs_path = input('Enter a linking ouputs path: ')
if not os.path.exists(linking_outputs_path):
    print('Linking outputs path does not exist.')
    exit()

with open(linking_outputs_path, "r") as f:
    linking_outputs = json.loads(f.read())
# news headlines dataset
with open("data/news_event_identication_dataset.json", "r") as f:
    input_data = json.loads(f.read())

# evaluate accuracy metrics
def evaluate(input_data, linking_outputs):
    # calculate hits
    hits = 0
    skipped = 0
    for headline in linking_outputs:
        # skip headlines not present in the dataset
        if headline not in input_data:
            skipped += 1
            continue
        for actual in input_data[headline]:
            actual = actual['id']
            if linking_outputs[headline] == actual:
                hits += 1
                break
    total = len(linking_outputs) - skipped
    return {'hits': hits,
            'total': total,
            'accuracy': hits / total}
    
metrics = evaluate(input_data, linking_outputs)

# get or create results file
result_path = "results/evaluation_results.csv"
if not os.path.exists(result_path):
    open(result_path, "x")
r_file = open(result_path, "r")
w_file = open(result_path, "a")

csv_writer = csv.writer(w_file)
if len(r_file.readlines()) == 0:
    headers = ["Methods", "Hits", "Accuracy"]
    csv_writer.writerow(headers)

basename = os.path.basename(linking_outputs_path)
basename = basename[:basename.index('.')]
method = basename[:basename.index('_output')]
csv_writer.writerow([method, metrics['hits'], metrics['accuracy']])

print('#######################################################')
print('Evaluation Results for %s' % os.path.basename(linking_outputs_path))
print('Hits: %s' % metrics['hits'])
print('Total: %s' % metrics['total'])
print('Accuracy: %s' % metrics['accuracy'])
print('#######################################################')

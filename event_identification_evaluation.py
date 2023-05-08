import json

# event concepts
with open("data/news_events_concepts.json", "r") as f:
    main_concepts = json.loads(f.read())
# news headlines dataset
with open("data/news_events_manual.json", "r") as f:
    input_data = json.loads(f.read())
# event linking method saved outputs
with open("data/event_linking_outputs.json", "r") as f:
    output_data = json.loads(f.read())

# score the methods.
def get_basic_scores(input_data, output_data):
    scores = {}
    for api in output_data:
        scores[api] = {}
        for headline in output_data[api]:
            scores[api][headline] = 0
            for actual in input_data[headline]:
                actual = actual['id']
                if output_data[api][headline] == actual:
                    scores[api][headline] += 1
                    break
    return scores

# evaluate accuracy metrics
def eval_basic(input_data, apis, get_scores):
    scores = get_scores(input_data, output_data)
    # evaluate
    metrics = {}
    for api in apis:
        summing = 0
        for headline in scores[api]:
            summing += scores[api][headline]
        metrics[api] = summing / len(input_data)
    return metrics

methods = [ "opentapioca", "falcon", "wikifier", "opentapioca_el", "falcon_el", "gptj_el", "gptj_el_types"]

metrics = eval_basic(input_data, methods, get_basic_scores)
with open('results/evaluation_results.json', "w") as f:
    json.dump(metrics, f)

print('#######################################################')
print('Accuracy Metrics:')
for method in metrics:
    print(method + ": " + str(metrics[method]))
print('#######################################################')
# An Evaluation Framework for Mapping News Headlines to Event Classes in a Knowledge Graph

This repository contains a curated news event linking dataset, output data from our event linking methods, an evaluation script, and the evaluation results for our linking methods.

## New Event Linking Corpus

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7909377.svg)](https://doi.org/10.5281/zenodo.7909377)

The dataset is available on Zenodo: https://doi.org/10.5281/zenodo.7909377

The dataset is provided in a JSON format. In this JSON object, the keys correspond to the news headlines and the values are a list of objects with fields `id` and `label`: `id` is the Wikidata QID of the annotated entity and `label` is the Wikidata label.

#### Example
```
{
    "Strong earthquake hits east of Acapulco, Mexico, 'people are worried'" : {
        "id": "Q7944",
        "label": "earthquake"
    }
}
```

## Evaluation Framework

Our evaluation framework consists of:
- A news event linking corpus that links news headlines to Wikidata entities: [data/news_event_identication_dataset.json](data/news_event_identication_dataset.json)
- Event linking data corresponding to a linking method provided in: [data/linking_outputs](data/linking_outputs). *The path to this file is provided as input to the evaluation script.*
- A script to calculate the accuracy metrics: [event_identification_evaluation.py](event_identification_evaluation.py)
- The metrics calculated from the evaluation script will be stored in: [results/](results/)

To run the evaluation script, call:
```
$python3 event_identification_evaluation.py
Enter a linking ouputs path: data/linking_outputs/{choose an output data file}
```

## License

This code base is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)

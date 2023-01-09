# MT-GenEval

This repository contains the data and code for the MT-GenEval benchmark, which evaluates gender translation accuracy on English -> {Arabic, French, German, Hindi, Italian, Portuguese, Russian, Spanish}. 
The MT-GenEval benchmark was released in the EMNLP 2022 paper [MT-GenEval: A Counterfactual and Contextual Dataset for Evaluating Gender Accuracy in Machine Translation](https://www.amazon.science/publications/mt-geneval-a-counterfactual-and-contextual-dataset-for-evaluating-gender-accuracy-in-machine-translation) by Anna Currey, Maria Nadejde, Raghavendra Pappagari, Mia Mayer, Stanislas Lauly, Xing Niu, Benjamin Hsu, and Georgiana Dinu.

## Citing
```
@inproceedings{currey-etal-2022-mtgeneval,
    title = "{MT-GenEval}: {A} Counterfactual and Contextual Dataset for Evaluating Gender Accuracy in Machine Translation",
    author = "Currey, Anna  and
      Nadejde, Maria  and
      Pappagari, Raghavendra  and
      Mayer, Mia  and
      Lauly, Stanislas,  and
      Niu, Xing  and
      Hsu, Benjamin  and
      Dinu, Georgiana",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    publisher = "Association for Computational Linguistics",
    url = ""https://arxiv.org/pdf/2211.01355.pdf,
}
```

## Data
The data is originally sourced from Wikipedia. 
We include sentence-level development and test segments in `data/sentences/` and inter-sentence test segments in `data/context/`. 

## Compute accuracy
To compute accuracy, call `accuracy_metric` function in `accuracy_metric.py`. Example usage for English-Russian contextual dataset is as follows
```
hypothesis_path = PATH_FOR_YOUR_SYSTEM_TRANSLATIONS
references_path = 'data/context/geneval-context-wikiprofessions-original-test.en_ru.ru'
flipped_references_path = 'data/context/geneval-context-wikiprofessions-flipped-test.en_ru.ru'
accuracy, metric_decisions = accuracy_metric(hypothesis_path, references_path, flipped_references_path)
```
For counterfactual dataset (the data in `data/sentences/`), metric decision can be obtained similarly but the accuracy computation is a little different as mentioned in Sec 3.1 of the paper. We consider a segment `Correct` only if both the original and the counterfactual segments are `Correct`. More specifically, 
```
_, metric_decisions_masculine = accuracy_metric(hypothesis_masculine_path, masculine_references_path, female_references_path)
_, metric_decisions_feminine = accuracy_metric(hypothesis_feminine_path, feminine_references_path, masculine_references_path)
accuracy, combined_decision = logicaloperation_AND(metric_decisions_masculine, metric_decisions_feminine)
```



## Security
See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License
The data and code are released under the CC-BY-SA-3.0 License. See [LICENSE](LICENSE) for details.

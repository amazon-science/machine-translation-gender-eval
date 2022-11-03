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

## Security
See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License
The data and code are released under the CC-BY-SA-3.0 License. See [LICENSE](LICENSE) for details.

# dev words

Check word frequency for studying English.

DEMO : https://ho4040.github.io/dev_words/

words extracted from

* RFC documents
* Python tutorial

## scrap RFC documents

```bash
$ mkdir data_source
$ python download_rfc_texts.py
```

## run

```bash
$ python words_freq.py > result.csv
```

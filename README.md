# dev words

Check word frequency for studying English.
words extracted from

* RFC documents
* Python tutorial

## Download data from RFC documents

```bash
$ mkdir data_source
$ python download_rfc_texts.py
```

## run

`words_freq.py` find all _txt_ files from `data_source` and `invalid_data_source`.
the Word that collected from `data_source` is evaluated as +1,
and the word that collected from `invalid_data_source` is evaluated as -1.
and then sort all words by sum of evaluated value.

```bash
$ python words_freq.py > result.csv
```

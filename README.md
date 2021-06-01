# MEDDOPROF-ST Baseline 1 - Lookup

## Introduction
This system extracts information from a set of annotated documents. Then, it checks whether, in a new set of text documents, the extracted annotation are present.
This system works as baseline for MEDDOPROF shared task [http://temu.bsc.es/meddoprof/].

#### Steps:
1. Extract annotations from Gold Standard .ann files and tokenize them.
2. For a new file, tokenize words.
3. Get the intersection between tokens in annotations and tokens in words.
4. For a token in the intersection, check surroundings of every occurrence in the text, to confirm whether there is a match with any annotation.
5. Repeat step 4 for every token in the intersection.
6. Repeat steps 2-5 for every file in the directory.

#### Input format
+ Gold standard files: folder with .ann files. 
+ Gold standard codes: .tsv file with the following format:
```
filename	text	span	code
```

+ Text files where labels will be predicted.


#### Output format
+ For tracks 1 and 2 (NER and CLASS), new .ann files are generated
+ For track 3 (NORM), a .tsv file is created with the same columns as the code list.

## Getting Started

Scripts written in Python 3.7, anaconda distribution Anaconda3-2019.07-Linux-x86_64.sh

### Prerequisites

You need to have installed python3 and its base libraries, plus:
+ pandas
+ os
+ csv
+ time
+ re
+ string
+ unicodedata
+ spacy

### Installing

```
git clone <repo_url>
```

## Usage

Both scripts accept the same two parameters:
+ --gs_path (-gs) specifies the path to the Gold Standard file.
+ --code_list (-cl) specifies the path to the Gold Standard codes list.
+ --data_path (-data) specifies the path to the text files.
+ --out_path (-out) specifies the path to the output predictions file.
+ --sub_track (-t) specifies the task we are using the system for: NER or CLASS.

```
$> python lookup.py -gs gold_standard/ -data datapath/ -out out_path/ -t TASK_NUMBER
```

## Contact
Antonio Miranda (antonio.miranda@bsc.es)
Salvador Lima (salvador.limalopez@gmail.com)

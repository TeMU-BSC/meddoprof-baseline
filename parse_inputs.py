#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:23:12 2020

@author: antonio, salva
"""
import os
import glob

import pandas as pd


def parse_ann(ann_folder):
    '''
    Parse folder with ANN files and create a DataFrame with every individual annotation

    Parameters
    ----------
    ann_folder : str
        Path to annotations folder

    Returns
    -------
    df_annot : Pandas DataFrame
        Parse annotations

    '''
    corpus = []
    for file in glob.glob(os.path.join(ann_folder, '**/*.ann'), recursive=True):
        with open(file, 'r') as f_in:
            for line in f_in.readlines():
                fields = line.split('\t')
                label, s_id, e_id = fields[1].split(' ')
                corpus.append([fields[0], s_id, e_id, label, fields[2].strip()])

    df_annot = pd.DataFrame(corpus, columns=['id', 's_id', 'e_id', 'type', 'text'])
    
    return df_annot

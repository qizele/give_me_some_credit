import pandas as pd
import numpy as np
import os
#Read one textfile with given sep, treat every column as string
def raw_readin(fileloc, dlm, start):
    datafile=pd.read_csv(fileloc, sep=dlm, header=start, dtype=float)
    return datafile

train_data=raw_readin('F:\Careers\Showcase\credit\cs-training.txt', ',' , 0)
test_data=raw_readin('F:\Careers\Showcase\credit\cs-test.txt', ',' , 0)



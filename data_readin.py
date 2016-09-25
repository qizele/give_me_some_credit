import pandas as pd
import numpy as np
import os
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

#Read one textfile with given sep, treat every column as string
def raw_readin(fileloc, dlm, start):
    datafile=pd.read_csv(fileloc, sep=dlm, header=start, dtype=float)
    return datafile

train_data=raw_readin('F:\Careers\Showcase\credit\cs-training.txt', ',' , 0)
test_data=raw_readin('F:\Careers\Showcase\credit\cs-test.txt', ',' , 0)

train_data.describe()

sns.distplot(train_data.loc[:,'RevolvingUtilizationOfUnsecuredLines'])
plt.show()
sns.distplot(train_data.loc[:,'age'])
plt.show()
sns.distplot(train_data.loc[:,'NumberOfTime30_59DaysPastDueNotWorse'])
plt.show()
sns.distplot(train_data.loc[:,'DebtRatio'])
plt.show()
sns.distplot(train_data.loc[~pd.isnull(train_data.loc[:,'MonthlyIncome']), 'MonthlyIncome'])
plt.show()
sns.distplot(train_data.loc[:,'NumberOfOpenCreditLinesAndLoans'])
plt.show()
sns.distplot(train_data.loc[:,'NumberOfTimes90DaysLate'])
plt.show()
sns.distplot(train_data.loc[:,'NumberRealEstateLoansOrLines'])
plt.show()
sns.distplot(train_data.loc[:,'NumberOfTime60_89DaysPastDueNotWorse'])
plt.show()
sns.distplot(train_data.loc[~pd.isnull(train_data.loc[:,'NumberOfDependents']),'NumberOfDependents'])
plt.show()

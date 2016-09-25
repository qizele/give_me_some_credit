#do the variable transformation for both train_data and test_data

#1) RevolvingUtilizationOfUnsecuredLines
col=train_data['RevolvingUtilizationOfUnsecuredLines'].dropna()
median_val=col.median()
train_data['RevolvingUtilizationOfUnsecuredLines'].fillna(value=median_val, inplace=True)
train_data.ix[train_data['RevolvingUtilizationOfUnsecuredLines']>1, 'RevolvingUtilizationOfUnsecuredLines']=1

train_data['RevolvingUtilizationOfUnsecuredLines_s1']=0.05-train_data['RevolvingUtilizationOfUnsecuredLines']
train_data.ix[train_data['RevolvingUtilizationOfUnsecuredLines_s1']<0, 'RevolvingUtilizationOfUnsecuredLines_s1']=0

train_data['RevolvingUtilizationOfUnsecuredLines_s2']=train_data['RevolvingUtilizationOfUnsecuredLines']-0.05
train_data.ix[train_data['RevolvingUtilizationOfUnsecuredLines_s2']<0, 'RevolvingUtilizationOfUnsecuredLines_s2']=0

test_data['RevolvingUtilizationOfUnsecuredLines'].fillna(value=median_val, inplace=True)
test_data.ix[test_data['RevolvingUtilizationOfUnsecuredLines']>1, 'RevolvingUtilizationOfUnsecuredLines']=1

test_data['RevolvingUtilizationOfUnsecuredLines_s1']=0.05-test_data['RevolvingUtilizationOfUnsecuredLines']
test_data.ix[test_data['RevolvingUtilizationOfUnsecuredLines_s1']<0, 'RevolvingUtilizationOfUnsecuredLines_s1']=0

test_data['RevolvingUtilizationOfUnsecuredLines_s2']=test_data['RevolvingUtilizationOfUnsecuredLines']-0.05
test_data.ix[test_data['RevolvingUtilizationOfUnsecuredLines_s2']<0, 'RevolvingUtilizationOfUnsecuredLines_s2']=0

 #2) age

col=train_data['age'].dropna()
median_val=col.median()
train_data['age'].fillna(value=median_val, inplace=True)
train_data.ix[train_data['age']>85, 'age']=85

test_data['age'].fillna(value=median_val, inplace=True)
test_data.ix[test_data['age']>85, 'age']=85

#3) NumberOfTime30_59DaysPastDueNotWorse

col=train_data['NumberOfTime30_59DaysPastDueNotWorse'].dropna()
median_val=col.median()
train_data['NumberOfTime30_59DaysPastDueNotWorse'].fillna(value=median_val, inplace=True)
train_data.ix[train_data['NumberOfTime30_59DaysPastDueNotWorse']>15, 'NumberOfTime30_59DaysPastDueNotWorse']=15

train_data['NumberOfTime30_59DaysPastDueNotWorse_0']=0
train_data.ix[train_data['NumberOfTime30_59DaysPastDueNotWorse']==0,'NumberOfTime30_59DaysPastDueNotWorse_0']=1

train_data['NumberOfTime30_59DaysPastDueNotWorse_s1']=7-train_data['NumberOfTime30_59DaysPastDueNotWorse']
train_data.ix[train_data['NumberOfTime30_59DaysPastDueNotWorse_s1']<0, 'NumberOfTime30_59DaysPastDueNotWorse_s1']=0

train_data['NumberOfTime30_59DaysPastDueNotWorse_s2']=train_data['NumberOfTime30_59DaysPastDueNotWorse']-7
train_data.ix[train_data['NumberOfTime30_59DaysPastDueNotWorse_s2']<0, 'NumberOfTime30_59DaysPastDueNotWorse_s2']=0

test_data['NumberOfTime30_59DaysPastDueNotWorse'].fillna(value=median_val, inplace=True)
test_data.ix[test_data['NumberOfTime30_59DaysPastDueNotWorse']>15, 'NumberOfTime30_59DaysPastDueNotWorse']=15

test_data['NumberOfTime30_59DaysPastDueNotWorse_0']=0
test_data.ix[test_data['NumberOfTime30_59DaysPastDueNotWorse']==0,'NumberOfTime30_59DaysPastDueNotWorse_0']=1

test_data['NumberOfTime30_59DaysPastDueNotWorse_s1']=7-test_data['NumberOfTime30_59DaysPastDueNotWorse']
test_data.ix[test_data['NumberOfTime30_59DaysPastDueNotWorse_s1']<0, 'NumberOfTime30_59DaysPastDueNotWorse_s1']=0

test_data['NumberOfTime30_59DaysPastDueNotWorse_s2']=test_data['NumberOfTime30_59DaysPastDueNotWorse']-7
test_data.ix[test_data['NumberOfTime30_59DaysPastDueNotWorse_s2']<0, 'NumberOfTime30_59DaysPastDueNotWorse_s2']=0

#4) DebtRatio

col=train_data['DebtRatio'].dropna()
median_val=col.median()
train_data['DebtRatio'].fillna(value=median_val, inplace=True)
train_data.ix[train_data['DebtRatio']>0.8, 'DebtRatio']=0.8

train_data['DebtRatio_s1']=0.2-train_data['DebtRatio']
train_data.ix[train_data['DebtRatio_s1']<0, 'DebtRatio_s1']=0

train_data['DebtRatio_s2']=train_data['DebtRatio']-0.2
train_data.ix[train_data['DebtRatio_s2']<0, 'DebtRatio_s2']=0

test_data['DebtRatio'].fillna(value=median_val, inplace=True)
test_data.ix[test_data['DebtRatio']>0.8, 'DebtRatio']=0.8

test_data['DebtRatio_s1']=0.2-test_data['DebtRatio']
test_data.ix[test_data['DebtRatio_s1']<0, 'DebtRatio_s1']=0

test_data['DebtRatio_s2']=test_data['DebtRatio']-0.2
test_data.ix[test_data['DebtRatio_s2']<0, 'DebtRatio_s2']=0

#5) MonthlyIncome

col=train_data['MonthlyIncome'].dropna()
median_val=col.median()
train_data['MonthlyIncome'].fillna(value=median_val, inplace=True)
train_data.ix[train_data['MonthlyIncome']>10000, 'MonthlyIncome']=10000

train_data['MonthlyIncome_s1']=3000-train_data['MonthlyIncome']
train_data.ix[train_data['MonthlyIncome_s1']<0, 'MonthlyIncome_s1']=0

train_data['MonthlyIncome_s2']=train_data['MonthlyIncome']-3000
train_data.ix[train_data['MonthlyIncome_s2']<0, 'MonthlyIncome_s2']=0

test_data['MonthlyIncome'].fillna(value=median_val, inplace=True)
test_data.ix[test_data['MonthlyIncome']>10000, 'MonthlyIncome']=10000

test_data['MonthlyIncome_s1']=3000-test_data['MonthlyIncome']
test_data.ix[test_data['MonthlyIncome_s1']<0, 'MonthlyIncome_s1']=0

test_data['MonthlyIncome_s2']=test_data['MonthlyIncome']-3000
test_data.ix[test_data['MonthlyIncome_s2']<0, 'MonthlyIncome_s2']=0

#6) NumberOfOpenCreditLinesAndLoans
col=train_data['NumberOfOpenCreditLinesAndLoans'].dropna()
median_val=col.median()
train_data['NumberOfOpenCreditLinesAndLoans'].fillna(value=median_val, inplace=True)
train_data.ix[train_data['NumberOfOpenCreditLinesAndLoans']>10, 'NumberOfOpenCreditLinesAndLoans']=10
train_data['NumberOfOpenCreditLinesAndLoans_sq']=train_data['NumberOfOpenCreditLinesAndLoans']*train_data['NumberOfOpenCreditLinesAndLoans']

test_data['NumberOfOpenCreditLinesAndLoans'].fillna(value=median_val, inplace=True)
test_data.ix[test_data['NumberOfOpenCreditLinesAndLoans']>10, 'NumberOfOpenCreditLinesAndLoans']=10
test_data['NumberOfOpenCreditLinesAndLoans_sq']=test_data['NumberOfOpenCreditLinesAndLoans']*test_data['NumberOfOpenCreditLinesAndLoans']

#7) NumberOfTimes90DaysLate
col=train_data['NumberOfTimes90DaysLate'].dropna()
median_val=col.median()
train_data['NumberOfTimes90DaysLate'].fillna(value=median_val, inplace=True)
train_data.ix[train_data['NumberOfTimes90DaysLate']>15, 'NumberOfTimes90DaysLate']=15
train_data['NumberOfTimes90DaysLate_0']=0
train_data.ix[train_data['NumberOfTimes90DaysLate']==0,'NumberOfTimes90DaysLate_0']=1

train_data['NumberOfTimes90DaysLate_s1']=5-train_data['NumberOfTimes90DaysLate']
train_data.ix[train_data['NumberOfTimes90DaysLate_s1']<0, 'NumberOfTimes90DaysLate_s1']=0

train_data['NumberOfTimes90DaysLate_s2']=train_data['NumberOfTimes90DaysLate']-5
train_data.ix[train_data['NumberOfTimes90DaysLate_s2']<0, 'NumberOfTimes90DaysLate_s2']=0

test_data['NumberOfTimes90DaysLate'].fillna(value=median_val, inplace=True)
test_data.ix[test_data['NumberOfTimes90DaysLate']>15, 'NumberOfTimes90DaysLate']=15
test_data['NumberOfTimes90DaysLate_0']=0
test_data.ix[test_data['NumberOfTimes90DaysLate']==0,'NumberOfTimes90DaysLate_0']=1

test_data['NumberOfTimes90DaysLate_s1']=5-test_data['NumberOfTimes90DaysLate']
test_data.ix[test_data['NumberOfTimes90DaysLate_s1']<0, 'NumberOfTimes90DaysLate_s1']=0

test_data['NumberOfTimes90DaysLate_s2']=test_data['NumberOfTimes90DaysLate']-5
test_data.ix[test_data['NumberOfTimes90DaysLate_s2']<0, 'NumberOfTimes90DaysLate_s2']=0

#8) NumberRealEstateLoansOrLines
col=train_data['NumberRealEstateLoansOrLines'].dropna()
median_val=col.median()
train_data['NumberRealEstateLoansOrLines'].fillna(value=median_val, inplace=True)
train_data['NumberRealEstateLoansOrLines_h']=0
train_data.ix[train_data['NumberRealEstateLoansOrLines']>10, 'NumberRealEstateLoansOrLines_h']=1
train_data['NumberRealEstateLoansOrLines_0']=0
train_data.ix[train_data['NumberRealEstateLoansOrLines']==0,'NumberRealEstateLoansOrLines_0']=1

train_data['NumberRealEstateLoansOrLines_s1']=6-train_data['NumberRealEstateLoansOrLines']
train_data.ix[train_data['NumberRealEstateLoansOrLines_s1']<0, 'NumberRealEstateLoansOrLines_s1']=0

train_data['NumberRealEstateLoansOrLines_s2']=train_data['NumberRealEstateLoansOrLines']-6
train_data.ix[train_data['NumberRealEstateLoansOrLines_s2']<0, 'NumberRealEstateLoansOrLines_s2']=0
train_data.ix[train_data['NumberRealEstateLoansOrLines_s2']>4, 'NumberRealEstateLoansOrLines_s2']=0

test_data['NumberRealEstateLoansOrLines'].fillna(value=median_val, inplace=True)
test_data['NumberRealEstateLoansOrLines_h']=0
test_data.ix[test_data['NumberRealEstateLoansOrLines']>10, 'NumberRealEstateLoansOrLines_h']=1
test_data['NumberRealEstateLoansOrLines_0']=0
test_data.ix[test_data['NumberRealEstateLoansOrLines']==0,'NumberRealEstateLoansOrLines_0']=1

test_data['NumberRealEstateLoansOrLines_s1']=6-test_data['NumberRealEstateLoansOrLines']
test_data.ix[test_data['NumberRealEstateLoansOrLines_s1']<0, 'NumberRealEstateLoansOrLines_s1']=0

test_data['NumberRealEstateLoansOrLines_s2']=test_data['NumberRealEstateLoansOrLines']-6
test_data.ix[test_data['NumberRealEstateLoansOrLines_s2']<0, 'NumberRealEstateLoansOrLines_s2']=0
test_data.ix[test_data['NumberRealEstateLoansOrLines_s2']>4, 'NumberRealEstateLoansOrLines_s2']=0

#9) NumberOfTime60_89DaysPastDueNotWorse
col=train_data['NumberOfTime60_89DaysPastDueNotWorse'].dropna()
median_val=col.median()
train_data['NumberOfTime60_89DaysPastDueNotWorse'].fillna(value=median_val, inplace=True)
train_data['NumberOfTime60_89DaysPastDueNotWorse_h']=0
train_data.ix[train_data['NumberOfTime60_89DaysPastDueNotWorse']>10, 'NumberOfTime60_89DaysPastDueNotWorse_h']=1
train_data['NumberOfTime60_89DaysPastDueNotWorse_0']=0
train_data.ix[train_data['NumberOfTime60_89DaysPastDueNotWorse']==0,'NumberOfTime60_89DaysPastDueNotWorse_0']=1

train_data['NumberOfTime60_89DaysPastDueNotWorse_s1']=6-train_data['NumberOfTime60_89DaysPastDueNotWorse']
train_data.ix[train_data['NumberOfTime60_89DaysPastDueNotWorse_s1']<0, 'NumberOfTime60_89DaysPastDueNotWorse_s1']=0

train_data['NumberOfTime60_89DaysPastDueNotWorse_s2']=train_data['NumberOfTime60_89DaysPastDueNotWorse']-6
train_data.ix[train_data['NumberOfTime60_89DaysPastDueNotWorse_s2']<0, 'NumberOfTime60_89DaysPastDueNotWorse_s2']=0
train_data.ix[train_data['NumberOfTime60_89DaysPastDueNotWorse_s2']>4, 'NumberOfTime60_89DaysPastDueNotWorse_s2']=0

test_data['NumberOfTime60_89DaysPastDueNotWorse'].fillna(value=median_val, inplace=True)
test_data['NumberOfTime60_89DaysPastDueNotWorse_h']=0
test_data.ix[test_data['NumberOfTime60_89DaysPastDueNotWorse']>10, 'NumberOfTime60_89DaysPastDueNotWorse_h']=1
test_data['NumberOfTime60_89DaysPastDueNotWorse_0']=0
test_data.ix[test_data['NumberOfTime60_89DaysPastDueNotWorse']==0,'NumberOfTime60_89DaysPastDueNotWorse_0']=1

test_data['NumberOfTime60_89DaysPastDueNotWorse_s1']=6-test_data['NumberOfTime60_89DaysPastDueNotWorse']
test_data.ix[test_data['NumberOfTime60_89DaysPastDueNotWorse_s1']<0, 'NumberOfTime60_89DaysPastDueNotWorse_s1']=0

test_data['NumberOfTime60_89DaysPastDueNotWorse_s2']=test_data['NumberOfTime60_89DaysPastDueNotWorse']-6
test_data.ix[test_data['NumberOfTime60_89DaysPastDueNotWorse_s2']<0, 'NumberOfTime60_89DaysPastDueNotWorse_s2']=0
test_data.ix[test_data['NumberOfTime60_89DaysPastDueNotWorse_s2']>4, 'NumberOfTime60_89DaysPastDueNotWorse_s2']=0

#10) NumberOfDependents
col=train_data['NumberOfDependents'].dropna()
median_val=col.median()
train_data['NumberOfDependents'].fillna(value=median_val, inplace=True)
train_data['NumberOfDependents_h']=0
train_data.ix[train_data['NumberOfDependents']>10, 'NumberOfDependents_h']=1

train_data['NumberOfDependents_s1']=5-train_data['NumberOfDependents']
train_data.ix[train_data['NumberOfDependents_s1']<0, 'NumberOfDependents_s1']=0

train_data['NumberOfDependents_s2']=train_data['NumberOfDependents']-5
train_data.ix[train_data['NumberOfDependents_s2']<0, 'NumberOfDependents_s2']=0
train_data.ix[train_data['NumberOfDependents_s2']>5, 'NumberOfDependents_s2']=0

test_data['NumberOfDependents'].fillna(value=median_val, inplace=True)
test_data['NumberOfDependents_h']=0
test_data.ix[test_data['NumberOfDependents']>10, 'NumberOfDependents_h']=1

test_data['NumberOfDependents_s1']=5-test_data['NumberOfDependents']
test_data.ix[test_data['NumberOfDependents_s1']<0, 'NumberOfDependents_s1']=0

test_data['NumberOfDependents_s2']=test_data['NumberOfDependents']-5
test_data.ix[test_data['NumberOfDependents_s2']<0, 'NumberOfDependents_s2']=0
test_data.ix[test_data['NumberOfDependents_s2']>5, 'NumberOfDependents_s2']=0



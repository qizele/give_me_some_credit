from sklearn.linear_model import *
from sklearn.metrics import *
import math
import random

def n_folds_sampling(datafile, n=3):
    index_set=datafile.index
    nrows=int(math.floor(len(datafile)/n))
    datapart=[]
    for i in range(0,n):
        if (i==n-1):
            rows=index_set
            datapart.append(datafile.loc[rows,:])
        else:
            rows=random.sample(list(index_set),nrows) 
            datapart.append(datafile.loc[rows,:])
            index_set=index_set.drop(rows)
    return datapart

def final_logistic_regression_model(datafile, target, nfold=3):
    datapart=[]
    datapart=n_folds_sampling(datafile, n=nfold)
    model=[]
    eval_metrics=[]
    for i in range(0,nfold):
        fold=datafile.drop(datapart[i].index)
        fold_target=fold[target]
        fold_data=fold.drop([target],axis=1)
        val_tar=datapart[i][target]
        val_data=datapart[i].drop([target],axis=1)
            
        m=LogisticRegression()
        m.fit(fold_data,fold_target)
        pred=m.predict_proba(val_data)[:,1]
        y_true=np.array(val_tar)
        eval_metrics.append(roc_auc_score(y_true, pred, average='weighted'))
        model.append(m)

    return model,eval_metrics


final_train_data_var=train_data_var.loc[:,['RevolvingUtilizationOfUnsecuredLines',
'RevolvingUtilizationOfUnsecuredLines_s2',
'age',
'DebtRatio',
'MonthlyIncome',
'MonthlyIncome_s2',
'DebtRatio_s2',
'NumberOfTimes90DaysLate_0',
'NumberOfTimes90DaysLate_s1',
'NumberOfTime30_59DaysPastDueNotWorse_s1',
'NumberOfTime30_59DaysPastDueNotWorse',
'NumberOfTimes90DaysLate',
'NumberOfOpenCreditLinesAndLoans_sq',
'NumberOfOpenCreditLinesAndLoans',
'NumberOfTime30_59DaysPastDueNotWorse_0',
'RevolvingUtilizationOfUnsecuredLines_s1',
'DebtRatio_s1',
'MonthlyIncome_s1',
'NumberOfDependents_s1',
'NumberOfDependents',
'NumberOfTime60_89DaysPastDueNotWorse_s1',
'NumberRealEstateLoansOrLines',
'NumberRealEstateLoansOrLines_s1',
'NumberOfTime60_89DaysPastDueNotWorse',
'NumberOfTime60_89DaysPastDueNotWorse_0',
'age_MonthlyIncome',
'age_DebtRatio',
'DebtRatio_MonthlyIncome',
'age_NumberOfTimes90DaysLate']]

final_train_data = pd.concat([final_train_data_var, train_target], axis=1)


final_test_data_var=test_data_var.loc[:,['RevolvingUtilizationOfUnsecuredLines',
'RevolvingUtilizationOfUnsecuredLines_s2',
'age',
'DebtRatio',
'MonthlyIncome',
'MonthlyIncome_s2',
'DebtRatio_s2',
'NumberOfTimes90DaysLate_0',
'NumberOfTimes90DaysLate_s1',
'NumberOfTime30_59DaysPastDueNotWorse_s1',
'NumberOfTime30_59DaysPastDueNotWorse',
'NumberOfTimes90DaysLate',
'NumberOfOpenCreditLinesAndLoans_sq',
'NumberOfOpenCreditLinesAndLoans',
'NumberOfTime30_59DaysPastDueNotWorse_0',
'RevolvingUtilizationOfUnsecuredLines_s1',
'DebtRatio_s1',
'MonthlyIncome_s1',
'NumberOfDependents_s1',
'NumberOfDependents',
'NumberOfTime60_89DaysPastDueNotWorse_s1',
'NumberRealEstateLoansOrLines',
'NumberRealEstateLoansOrLines_s1',
'NumberOfTime60_89DaysPastDueNotWorse',
'NumberOfTime60_89DaysPastDueNotWorse_0',
'age_MonthlyIncome',
'age_DebtRatio',
'DebtRatio_MonthlyIncome',
'age_NumberOfTimes90DaysLate']]

model,eval_metrics=final_logistic_regression_model(final_train_data, 'SeriousDlqin2yrs', nfold=3)
model[0].intercept_
model[0].coef_.T
model[1].intercept_
model[1].coef_.T
model[2].intercept_
model[2].coef_.T

#prediction based on test data
test_pred=(model[0].predict_proba(final_test_data_var)[:,1]+model[1].predict_proba(final_test_data_var)[:,1]+model[2].predict_proba(final_test_data_var)[:,1])/3
test_pred=pd.DataFrame(test_pred)
test_pred.index=test_pred.index+1
test_pred.to_csv('F:\Careers\Showcase\credit\outresult.txt', sep=',', header=False, index=True)



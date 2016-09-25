from sklearn.ensemble import *
from sklearn.metrics import *

def twoway_interation(datafile, varlist=[]):
    if (varlist==[]):
        datatypes=dict(datafile.dtypes)
        for i,v in datatypes.items():
            if((str(v)[:5]=='float')or(str(v)[:3]=='int')):
                varlist.append(i)

    for i in range(0,len(varlist)):
        for j in range(i+1,len(varlist)):
            col_name=varlist[i]+'_'+varlist[j]
            col_var=datafile[varlist[i]]*datafile[varlist[j]]
            if (max(col_var)==0)and(min(col_var)==0):
                pass
            else:
                datafile[col_name]=col_var                
    return datafile

twoway_interation(train_data_var, varlist=['age','DebtRatio','RevolvingUtilizationOfUnsecuredLines','MonthlyIncome','NumberOfTimes90DaysLate'])
twoway_interation(test_data_var, varlist=['age','DebtRatio','RevolvingUtilizationOfUnsecuredLines','MonthlyIncome','NumberOfTimes90DaysLate'])


rf=RandomForestClassifier(n_estimators=500,max_features='sqrt',class_weight='balanced').fit(train_data_var,train_target)

imp=rf.feature_importances_
imp=pd.Series(imp,name='importance')
feature=pd.Series(train_data_var.columns, name='feature')
var_imp=pd.concat([feature,imp], axis=1)
var_imp.sort_values(by='importance', ascending=False,inplace=True)

#plot univeriant chart for two way interaction

def univariate_plot(data, n_bin, response, var, alpha=0.5):
    #Step 1 - Sort the data
    var_data=data.loc[:,[response,var]]
    var_data.sort_values(by=var,ascending=True, inplace=True)
    var_data.reset_index(inplace=True, drop=True)
    #Step 2 - Create a bin for missing value if any
    missing_len=len(data.loc[pd.isnull(data.loc[:,var])])
    bin_var=[]
    bin_response=[]
    bin_count=[]
    if missing_len>0:
        bin_count.append(missing_len)
        bin_var.append(-999999) 
        sum_response=sum(data.loc[pd.isnull(data.loc[:,var]), response])
        bin_response.append(np.log((sum_response+alpha)/(missing_len-sum_response+alpha)))
    
    #Step 3 - Create bins, counts, mean_var, and elogit
    var_data.dropna(axis=0, how='any', inplace=True)
    length=len(var_data)
    n_piece=length/n_bin
    for i in range(0,n_bin,1):
        if i<n_bin-1:
            bin_count.append(n_piece)
            bin_var.append(sum(var_data.loc[i*n_piece:(i+1)*n_piece-1,var])/n_piece)
            sum_response=sum(var_data.loc[i*n_piece:(i+1)*n_piece-1,response])
            bin_response.append(np.log((sum_response+alpha)/(n_piece-sum_response+alpha)))
        else:
            n_final=length-i*n_piece
            bin_count.append(n_final)
            bin_var.append(sum(var_data.loc[i*n_piece:length-1,var])/n_final)
            sum_response=sum(var_data.loc[i*n_piece:length-1,response])
            bin_response.append(np.log((sum_response+alpha)/(n_final-sum_response+alpha)))
    #Step 4: Create and return output
    output=pd.DataFrame({'counts' :bin_count,'mean_var' :bin_var,'mean_resp':bin_response})
    return output

#example os age*monthly_income
train_data_young=train_data[train_data.age<=40]
train_data_mid=train_data[(train_data.age>40)&(train_data.age<=60)]
tran_data_senior=train_data[train_data.age>60]

output_income_young=univariate_plot(train_data_young, 20, 'SeriousDlqin2yrs', 'MonthlyIncome')
output_income_mid=univariate_plot(train_data_mid, 20, 'SeriousDlqin2yrs', 'MonthlyIncome')
output_income_senior=univariate_plot(tran_data_senior, 20, 'SeriousDlqin2yrs', 'MonthlyIncome')



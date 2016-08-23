####Univariate Plot for Binary Response (plotting elogit)##############
import pandas as pd
import numpy as np

def univariate_plot(data, n_bin, response, var, alpha=0.5):
    #Step 1 - Sort the data
    var_data=data.loc[:,[response,var]]
    var_data.sort_values(by=var,ascending=True, inplace=True)
    var_data.reset_index(inplace=True, drop=True)
    #Step 2 - Create a bin for missing value if any
    missing_len=len(data.loc[pd.isnull(data.loc[:,var])])
    if missing_len>0:
        bin_count.append(missing_len)
        bin_var.append(-999999) 
        sum_response=sum(data.loc[pd.isnull(data.loc[:,var]), response])
        bin_response.append(np.log((sum_response+alpha)/(missing_len-sum_response+alpha)))
    
    #Step 3 - Create bins, counts, mean_var, and elogit
    var_data.dropna(axis=0, how='any', inplace=True)
    length=len(var_data)
    n_piece=length/n_bin
    bin_var=[]
    bin_response=[]
    bin_count=[]
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

#get univariate plot for each independent variable
output_util=univariate_plot(train_data, 20, 'SeriousDlqin2yrs', 'RevolvingUtilizationOfUnsecuredLines')
output_age=univariate_plot(train_data, 20, 'SeriousDlqin2yrs', 'age')
output_pastdue30_59=univariate_plot(train_data, 20, 'SeriousDlqin2yrs', 'NumberOfTime30_59DaysPastDueNotWorse')
output_debt_ratio=univariate_plot(train_data, 20, 'SeriousDlqin2yrs', 'DebtRatio')
output_income=univariate_plot(train_data, 20, 'SeriousDlqin2yrs', 'MonthlyIncome')
output_line=univariate_plot(train_data, 20, 'SeriousDlqin2yrs', 'NumberOfOpenCreditLinesAndLoans')
output_late_90=univariate_plot(train_data, 20, 'SeriousDlqin2yrs', 'NumberOfTimes90DaysLate')
output_late_90=univariate_plot(train_data, 20, 'SeriousDlqin2yrs', 'NumberOfTimes90DaysLate')
output_real_estate=univariate_plot(train_data, 20, 'SeriousDlqin2yrs', 'NumberRealEstateLoansOrLines')
output_pastdue60_89=univariate_plot(train_data, 20, 'SeriousDlqin2yrs', 'NumberOfTime60_89DaysPastDueNotWorse')
output_Dependents=univariate_plot(train_data, 20, 'SeriousDlqin2yrs', 'NumberOfDependents')


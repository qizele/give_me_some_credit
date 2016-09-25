####Univariate Plot for Binary Response (plotting elogit)##############
import pandas as pd
import numpy as np

def univariate_plot(data, response, var, alpha=0.5):
    #Step 1 - Sort the data
    var_data=data.loc[:,[response,var]]
    group_count=pd.DataFrame(var_data.groupby([var])[response].count().reset_index())
    group_sum=pd.DataFrame(var_data.groupby([var])[response].sum().reset_index())
    group_all=pd.merge(group_count, group_sum, on=var)
    group_all.columns=[var, 'count', 'sum']
    group_all['mean_resp']=np.log((group_all['sum']+alpha)/(group_all['count']-group_all['sum']+alpha))
    #Step 4: Create and return output
    output=group_all.loc[:,(var,'mean_resp')]
    return output

#get univariate plot for each independent variable

output_pastdue30_59=univariate_plot(train_data, 'SeriousDlqin2yrs', 'NumberOfTime30_59DaysPastDueNotWorse')
output_late_90=univariate_plot(train_data, 'SeriousDlqin2yrs', 'NumberOfTimes90DaysLate')
output_real_estate=univariate_plot(train_data, 'SeriousDlqin2yrs', 'NumberRealEstateLoansOrLines')
output_pastdue60_89=univariate_plot(train_data, 'SeriousDlqin2yrs', 'NumberOfTime60_89DaysPastDueNotWorse')
output_Dependents=univariate_plot(train_data, 'SeriousDlqin2yrs', 'NumberOfDependents')


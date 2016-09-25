from sklearn.ensemble import *
from sklearn.metrics import *

def all_numeric_check(datafile):
    output=True
    nonum_list=[]
    datatypes=dict(datafile.dtypes)
    for i,v in datatypes.items():
        if (str(v)[:5]!='float')and(str(v)[:3]!='int'):
            output=False
            nonum_list.append(i)
            
    if (output==True):
        print("all numeric variable")
    elif(output==False):
        print("The following are not numeric variables: ")
        for i in nonum_list:
            print(i)

all_numeric_check(train_data)
all_numeric_check(test_data)
train_target=train_data['SeriousDlqin2yrs']
train_data_var=train_data.drop(['SeriousDlqin2yrs','id'],axis=1)

test_target=test_data['SeriousDlqin2yrs']
test_data_var=test_data.drop(['SeriousDlqin2yrs','id'],axis=1)


rf=RandomForestClassifier(n_estimators=500,max_features='sqrt',class_weight='balanced').fit(train_data_var,train_target)

imp=rf.feature_importances_
imp=pd.Series(imp,name='importance')
feature=pd.Series(train_data_var.columns, name='feature')
var_imp=pd.concat([feature,imp], axis=1)
var_imp.sort_values(by='importance', ascending=False,inplace=True)
    

import pandas as pd
import numpy as np
import random
import math
from sklearn import tree

cart_data=train_data.fillna(value=-999)
target=cart_data['SeriousDlqin2yrs']
cart_train_data=cart_data.drop(['SeriousDlqin2yrs','id'],axis=1)
tree_model=tree.DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=3, min_samples_split=2)
tree_model=tree_model.fit(cart_train_data, target)

#######Codes from Stackoverflow and worked#############
def get_code(tree, feature_names):
        left      = tree.tree_.children_left
        right     = tree.tree_.children_right
        threshold = tree.tree_.threshold
        features  = [feature_names[i] for i in tree.tree_.feature]
        value = tree.tree_.value

        def recurse(left, right, threshold, features, node):
                if (threshold[node] != -2):
                        print ("if ( " + features[node] + " <= " + str(threshold[node]) + " ) {")
                        if left[node] != -1:
                                recurse (left, right, threshold, features,left[node])
                        print ("} else {")
                        if right[node] != -1:
                                recurse (left, right, threshold, features,right[node])
                        print ("}")
                else:
                        print ("return " + str(value[node]))

        recurse(left, right, threshold, features, 0)


get_code(tree_model, cart_train_data.columns)

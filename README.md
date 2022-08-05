# Predicting Intensive Care Unit (ICU) length of stay as continous variable
In this code, we perform a full cleaning and predictive model deployment. 

We wrote a nested-cross validation code doing grid search. 
The GridSearch function was not optimal and it was taking too long. 
Our in-house code worked way faster and it is simply based on nested for loops
Permutation based and tree based feature importance are there
This code is for SVM and XGboost because they had slightly different fitting methods. For other regressors, just change the regressor name and input their variables and ranges

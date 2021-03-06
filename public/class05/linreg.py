# linreg.py

# This script should do linear regression.
# Demo:
# python linreg.py

import pandas as pd
import numpy  as np

# As of today, allpredictions.csv contains 8955 rows.
# 8900 - 2600 is 6300 is 6300 days is 25 years.
# I should learn from 25 years of data:
csv_df = pd.read_csv('http://www.spy611.com/csv/allpredictions.csv')[2599:8900]

train_df = csv_df[['pctlead', 'pctlag1', 'pctlag2', 'pctlag4', 'pctlag8', 'pctlag16']]
train_a  = np.array(train_df)

x_train_a = train_a[:,1:]
pctlead_a = train_a[:,0]

# Now I should learn from x_train_a,pctlead_a:
from sklearn import linear_model
clf_lr = linear_model.LinearRegression()
clf_lr.fit(x_train_a, pctlead_a)

print('Intercept:')
print(clf_lr.intercept_)
print('Coefficients:')
print(clf_lr.coef_)
# The above model assumes that pctlead relies somewhat on pctlag1,2,4,8,16

# Now I should predict one observation (quiet day):
just1x = [[0.001, 0.001, 0.001, 0.001, 0.001]]
pctlead_prediction = clf_lr.predict(just1x)[0]
print('quiet day prediction:')
print(pctlead_prediction)

# Now I should predict one observation (strong down day):
just1x = [[-2.1, -2.2, -2.4, -2.8, -2.16]]
pctlead_prediction = clf_lr.predict(just1x)[0]
print('down day prediction:')
print(pctlead_prediction)

# Now I should predict one observation (strong up day):
just1x = [[2.1, 2.2, 2.4, 2.8, 2.16]]
pctlead_prediction = clf_lr.predict(just1x)[0]
print('up day prediction:')
print(pctlead_prediction)

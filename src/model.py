import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor

from sklearn.metrics import recall_score, precision_score, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import linear_model

from sklearn.metrics import mean_squared_error

df = pd.read_csv('formodel.csv',encoding = "ISO-8859-1")

df.columns

# Index(['L_Region', 'Domain', 'Percentage_Attending_From_Home',
#        'Percentage_Attending_NOT_from_Home', 'Attendance'],
#       dtype='object')
#


#Prepare for Decision Tree then Random Forest
#Need to Dummieize L_Region, and Domain
#Percentage and Percentage not are colinear (sum to 1) - so I'll keep just Per att from Home.
#y is total result

y = df.pop('Attendance')
#d=df.pop('Percentage_Attending_From_Home')
cols_to_transform = [ 'L_Region', 'Domain' ]
just_dummies = pd.get_dummies(df[cols_to_transform])
just_dummies.shape
just_dummies.drop(['Domain_Planning & Finance', 'L_Region_Western Canada'], inplace=True, axis=1)
just_dummies.shape
dfkeep = df[['Percentage_From_Home_Region','EventYear']]
step_1 = pd.concat([dfkeep, just_dummies], axis=1)
#step_1.drop(['L_Region', 'Domain' ], inplace=True, axis=1) #Drop original non dummies
#step_1.drop(['Percentage_Attending_NOT_from_Home'], inplace=True, axis=1)
X=step_1
y =np.array(y)
X=np.array(X)

X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=40)


#Random Forest Regressor
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
rf_score = rf.score(X_test,y_test)  #accuracy
y_predict = rf.predict(X_test)

root_mean_sq_error_rf = mean_squared_error(y_test, y_predict)**0.5






#Basic DecisionTreeRegressor
dt = DecisionTreeRegressor()
dt.fit(X_train, y_train)
dt_predict = dt.predict(X_test)
dt_score = dt.score(X_test, y_test)
y_predict = dt.predict(X_test)
root_mean_sq_error_dt = mean_squared_error(y_test, y_predict)**0.5

#Try Linear Model
#instantiate linear model for ease of coding below

lm = linear_model.LinearRegression()

#generate fit of model base on training set
#fit method expects two arguments of x’s and y’s

model = lm.fit(X_train, y_train)

#generate predicted values of y_test from X_test based off of training set

y_predict = lm.predict(X_test)
root_mean_sq_error_lm = mean_squared_error(y_test, y_predict)**0.5
print("Root Mean Squared Error")
print("Linear",root_mean_sq_error_lm)
print("Decision Tree",root_mean_sq_error_dt)
print("Random Forest",root_mean_sq_error_rf)
#plotting predicted ys against y values in test set




#try dropping these two
#Planning & Finance
#Western Canada

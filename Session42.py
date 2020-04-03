import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

dataSet = pd.DataFrame()

# Attribute: outlook
dataSet['Outlook'] = ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy',
                      'Sunny', 'Overcast', 'Overcast', 'Rainy']

# Attribute: temperature
dataSet['Temperature'] = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild']

# Attribute: humidity
dataSet['Humidity'] = ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High']

# Attribute: windy
dataSet['Windy'] = ['False', 'True', 'False', 'False', 'False', 'True', 'True', 'False', 'False', 'False', 'True', 'True', 'False', 'True']

# Attribute: play
dataSet['Play']= ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']


print(dataSet)

# Dummy Variables :- Its a technique where we represent categorical data with numerical data
# Dummy variables are sometimes also known as Indicator Variable

# ONE-HOT :- Technique In ML where categorical data is represented as 1 or 0

"""


     Outlook Temperature Humidity  Windy Play
0      Sunny         Hot     High  False   No
1      Sunny         Hot     High   True   No
2   Overcast         Hot     High  False  Yes
3      Rainy        Mild     High  False  Yes
4      Rainy        Cool   Normal  False  Yes
5      Rainy        Cool   Normal   True   No
6   Overcast        Cool   Normal   True  Yes
7      Sunny        Mild     High  False   No
8      Sunny        Cool   Normal  False  Yes
9      Rainy        Mild   Normal  False  Yes
10     Sunny        Mild   Normal   True  Yes
11  Overcast        Mild     High   True  Yes
12  Overcast         Hot   Normal  False  Yes
13     Rainy        Mild     High   True   No

Outlook_Sunny     Outlook_Overcast   Outlook_Rainy

"""
one_hot_data = pd.get_dummies(dataSet[ ['Outlook', 'Temperature',
                              'Humidity', 'Windy'] ])
print(one_hot_data)
# print(one_hot_data['outlook_sunny'])

x_train, x_test, y_train, y_test = train_test_split(one_hot_data, dataSet['Play'], test_size=0.2, random_state=1)

# Model Creation
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)

# Percentage Score :) How Accurate the Model IS ?
print(">> Accuracy Score:", metrics.accuracy_score(y_test, y_pred))

# Test the Model Manually with these inputs and tell me the class
# outlook = sunny, temperature = hot, humidity = normal, windy = false
# Predict can we play outside or not ?

inputData = [0, 0, 1, 0, 1, 0, 0, 1, 1, 0]
predictedClass = model.predict([inputData])
print(">> Predicted Class for", inputData, "is:", predictedClass)
import pandas as pd
import numpy as np

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


def computeEntropyDataSet():

    # E(S) = -P(Yes) * log_base2(P(Yes)) - P(No) * log_base2(P(No))
    # E(S) = -9/14 * log_base2(9/14) - 5/14 * log_base2(5/14)


    # print(len(dataSet['play']))
    # print(len(dataSet[dataSet['play'] == 'yes']))
    # print(len(dataSet[dataSet['play'] == 'no']))

    """
    total = len(dataSet['play'])
    numOfYes = len(dataSet[dataSet['play'] == 'yes'])
    numOfNo = len(dataSet[dataSet['play'] == 'no'])
    probabilityYes = numOfYes / total
    probabilityNo = numOfNo / total
    print(probabilityYes)
    print(probabilityNo)
    entropy = -(probabilityYes*np.log2(probabilityYes)) - (probabilityNo*np.log2(probabilityNo))
    print(entropy)
    return entropy
    """

    return  -( (len(dataSet[dataSet['Play'] == 'Yes']) / len(dataSet['Play']) ) * np.log2( (len(dataSet[dataSet['Play'] == 'Yes']) / len(dataSet['Play']) ) ))  - ( (len(dataSet[dataSet['Play'] == 'No']) / len(dataSet['Play']) ) * np.log2( (len(dataSet[dataSet['Play'] == 'No']) / len(dataSet['Play']) ) ))

    def informationGainInOutlook():
        pass


print("Entropy Of Data Set:", computeEntropyDataSet())
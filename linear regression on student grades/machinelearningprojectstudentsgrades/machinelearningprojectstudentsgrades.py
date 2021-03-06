
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import pickle 
from sklearn import linear_model
from sklearn.utils import shuffle
from matplotlib import style


dataset = pd.read_csv('student-mat.csv',sep = ";")
data= dataset[["G1","G2","G3","studytime","failures","absences"]]
predict = "G3"

X=np.array(data.drop([predict], 1))
Y=np.array(data[predict])

x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(X,Y,test_size =0.1)

linear = linear_model.LinearRegression()
linear.fit(x_train,y_train)
accuracy = linear.score(x_test, y_test)
print(accuracy)



print("Co: \n",linear.coef_)
print("Intercept:\n",linear.intercept_)

predictions = linear.predict(x_test)

#for x in range(len(predictions)):
 #   print(predictions[x],x_test[x],y_test[x])

p = 'studytime'
style.use("ggplot")
plt.scatter(data[p],data["G3"])
plt.xlabel(p)
plt.ylabel("Final Grade")
plt.show()
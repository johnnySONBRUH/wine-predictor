from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
model = RandomForestClassifier(random_state=42,n_estimators=100)
data = pd.read_csv('data.csv')
data.drop(inplace=True,columns=['Id'])
X = data
X = X.drop(columns=['quality'])
Y = data
Y = Y.drop(columns=['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol'])
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
model.fit(x_train,y_train)
pred = model.predict(x_test)git add .
git commit -m 'TEMPORARY COMMIT'
git push
acc = accuracy_score(y_test,pred)
print(acc)
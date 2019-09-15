import data
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

X, y = data.load()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=42)
model = AdaBoostClassifier()
model.fit(X_train, y_train)

joblib.dump(model, 'model2000d.joblib')






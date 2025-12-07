# Full script: Labs 2, 3, 4, 6 – Cleaned, Reviewed, and Fixed for non-interactive environment

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score, KFold, LeaveOneOut
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from ISLP import load_data

# ---------------------------
# Lab 2: Classification (Logistic, LDA, QDA)
# ---------------------------
Smarket = load_data('Smarket')
Smarket['Direction_bin'] = (Smarket['Direction'] == 'Up').astype(int)
train = Smarket[Smarket['Year'] < 2005]
test = Smarket[Smarket['Year'] >= 2005]

# Logistic Regression
logit_mod = smf.glm('Direction_bin ~ Lag1 + Lag2 + Volume', data=train, family=sm.families.Binomial()).fit()
logit_pred = logit_mod.predict(test[['Lag1','Lag2','Volume']])
logit_class = np.where(logit_pred > 0.5, 'Up', 'Down')

# LDA
lda = LDA()
lda.fit(train[['Lag1','Lag2']], train['Direction'])
lda_pred = lda.predict(test[['Lag1','Lag2']])

# QDA
qda = QDA()
qda.fit(train[['Lag1','Lag2']], train['Direction'])
qda_pred = qda.predict(test[['Lag1','Lag2']])

print("Logistic Confusion:\n", confusion_matrix(test['Direction'], logit_class))
print("LDA Confusion:\n", confusion_matrix(test['Direction'], lda_pred))
print("QDA Confusion:\n", confusion_matrix(test['Direction'], qda_pred))

# ---------------------------
# Lab 3: Cross-validation
# ---------------------------
Auto = load_data('Auto')
X = Auto[['horsepower']]
y = Auto['mpg']

# LOOCV with linear regression
loo = LeaveOneOut()
linreg = LinearRegression()
scores = cross_val_score(linreg, X, y, cv=loo, scoring='neg_mean_squared_error')
print("LOOCV MSE:", -np.mean(scores))

# 10-fold CV with polynomial regression
kf = KFold(n_splits=10, shuffle=True, random_state=1)
for degree in range(1,6):
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    scores = cross_val_score(model, X, y, cv=kf, scoring='neg_mean_squared_error')
    print(f"Degree {degree} 10-fold CV MSE:", -np.mean(scores))

# ---------------------------
# Lab 4: Ridge, Lasso, Elastic Net, PCA
# ---------------------------
Hitters = load_data('Hitters').dropna()
X_hit = Hitters.drop(columns=['Salary']).select_dtypes(include=np.number).fillna(0)
y_hit = Hitters['Salary']

# Ridge
ridge = Pipeline([
    ('scaler', StandardScaler()),
    ('ridge', Ridge(alpha=10))
])
ridge.fit(X_hit, y_hit)
print("Ridge Coefs:\n", ridge.named_steps['ridge'].coef_)

# Lasso
lasso = Pipeline([
    ('scaler', StandardScaler()),
    ('lasso', Lasso(alpha=0.1, max_iter=10000))
])
lasso.fit(X_hit, y_hit)
print("Lasso Coefs:\n", lasso.named_steps['lasso'].coef_)

# Elastic Net
elastic = Pipeline([
    ('scaler', StandardScaler()),
    ('elastic', ElasticNet(alpha=0.1, l1_ratio=0.5, max_iter=10000))
])
elastic.fit(X_hit, y_hit)
print("Elastic Net Coefs:\n", elastic.named_steps['elastic'].coef_)

# PCA on Auto data
X_auto = Auto[['cylinders','displacement','horsepower','weight','acceleration']].dropna()
X_scaled = StandardScaler().fit_transform(X_auto)
pca = PCA()
pca.fit(X_scaled)
print("PCA explained variance ratios:", pca.explained_variance_ratio_)

# ---------------------------
# Lab 6: Trees
# ---------------------------
Boston = load_data('Boston')
X_boston = Boston.drop(columns=['medv'])
y_boston = Boston['medv']
tree = DecisionTreeRegressor(max_depth=3, random_state=0)
tree.fit(X_boston, y_boston)
plt.figure(figsize=(12,8))
plot_tree(tree, feature_names=X_boston.columns, filled=True)
plt.savefig('boston_tree.png')  # Fix: save figure instead of plt.show()

Carseats = load_data('Carseats')
Carseats['High'] = np.where(Carseats.Sales > 8, 'Yes', 'No')
X_carseats = pd.get_dummies(Carseats.drop(columns=['Sales','High']), drop_first=True)
y_carseats = Carseats['High']
clf = DecisionTreeClassifier(max_depth=3, random_state=0)
clf.fit(X_carseats, y_carseats)
plt.figure(figsize=(12,8))
plot_tree(clf, feature_names=X_carseats.columns, class_names=clf.classes_, filled=True)
plt.savefig('carseats_tree.png')  # Fix: save figure instead of plt.show()
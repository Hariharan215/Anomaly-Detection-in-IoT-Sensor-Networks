# Instanciate selector
selector = SelectKBest(chi2, k=10) # select k = 11 < 51

# Fit it to data
X_fitted = selector.fit_transform(X, one_hot['NORMAL'])

# Determine k-best features
mask = selector.get_support() #list of booleans
new_features = [] # The list of your K best features

feature_names = list(X.columns.values)

for bool, feature in zip(mask, feature_names):
    if bool:
        new_features.append(feature)

X_fitted = X.iloc[:,new_features]
X_fitted.head()

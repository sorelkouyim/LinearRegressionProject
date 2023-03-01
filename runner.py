## Get X and y
X,y= get_data()

Q, R = cgs(X)
b = np.matmul( np.transpose(Q), y )

theta = backsubs(R, b)

## Test on Add ones to X
X= add_ones(X)
X

# splitting the files
X_train, X_test, y_train, y_test= split_data(X, y, 0.8)


# Instanciate the LinearRegression class 
model= LinearRegression()


# Train the model
# X_train, X_test, y_train, y_test
model.fit(X_train,y_train)


# Make a prediction on X_test
y_pred =model.predict(X_test)


# Compute the MSE (Evaluate both, regression and classification)
value = mse(y_test, y_pred)
value


modelNormal= LinearRegression(False)

# training the data set
modelNormal.fit(X_train,y_train)

# Predicting the data set
y_pred =modelNormal.predict(X_test)
# y_pred

# Result of normal equation
val = normalEquation(X_train, y_train)
val

# Result of Matrix multiplication of X_test and predicted theta 
y_pred_norm=np.matmul(X_test, val)


# Competing the mean square error

value = mse(y_test, y_pred_norm)
value
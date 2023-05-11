import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the CSV file
df = pd.read_csv(r'data/data_for_ANN_Fitting.csv')


# Get the features and target variables
X = df[['M', 'logR', 'PGA', 'Ia', 'CAV']].values
y = df['MMI'].values

# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)

# Print the coefficients
print(model.coef_)
print(model.intercept_)
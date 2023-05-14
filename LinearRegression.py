import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the CSV file
df = pd.read_csv(r'data/data.csv')

# Get the features and target variables
X = df[['M', 'logR', 'PGA', 'Ia', 'CAV']].values
y = df['MMI'].values

# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)

# Print the equation
print(f"MMI = {model.intercept_:.3f} + {model.coef_[0]:.3f}M - {model.coef_[1]:.3f}logR + {model.coef_[2]:.3f}PGA + {model.coef_[3]:.3f}Ia - {model.coef_[4]:.3f}CAV")


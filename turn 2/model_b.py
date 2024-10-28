import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load data
data = pd.read_csv('customer_purchases.csv')

# Preprocess data
data = data.dropna()
data = pd.get_dummies(data, columns=['product'])

# Define features and target
features = data.drop(columns=['customer_id', 'purchase_date', 'target'])
target = data['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train a decision tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")


# Function to suggest cross-sell products
def suggest_cross_sell(purchase_history):
    # Preprocess the purchase history for prediction
    purchase_history_df = pd.DataFrame(purchase_history, columns=['product'])
    purchase_history_df = pd.get_dummies(purchase_history_df, columns=['product'])

    # Predict cross-sell recommendations
    recommendations = model.predict_proba(purchase_history_df)[:, 1] > 0.5

    # Return recommended product IDs
    return [i for i, r in enumerate(recommendations) if r]


# Example usage:
purchase_history = [1, 3, 5]  # Customer has bought products 1, 3, and 5
recommendations = suggest_cross_sell(purchase_history)
print("Recommended Products:", recommendations)

"""
Assignment-01 - Programming Question 2
KNeighborsClassifier on the Wine dataset
"""

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load the wine dataset
wine = load_wine()
X = wine.data
y = wine.target

# Split into train (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train KNeighborsClassifier with k=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Calculate and print test accuracy
accuracy = knn.score(X_test, y_test)
print("Test Accuracy:", round(accuracy, 4))
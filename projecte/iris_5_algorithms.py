import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# ===== LOAD DATASET =====
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['species'] = data.target

print("=" * 60)
print("           DATASET: IRIS")
print("=" * 60)
print(f"Total Rows    : {df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")
print(f"Classes       : Setosa (0), Versicolor (1), Virginica (2)")
print("\nFirst 10 Rows of Dataset:")
print("-" * 60)
print(df.head(10).to_string(index=False))
print("=" * 60)

# Split data for supervised algorithms
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Dictionary to store accuracies for final comparison
accuracies = {}

# ===================================================
# ALGORITHM 1: LOGISTIC REGRESSION
# ===================================================
print("\n" + "-" * 60)
print("   ALGORITHM 1: LOGISTIC REGRESSION")
print("-" * 60)
print("""
Description:
  Logistic Regression is a classification algorithm used to
  predict which category/class an input belongs to. Despite
  having 'regression' in its name, it is used for classification.
  It calculates the probability of an input belonging to a class
  and assigns it to the class with the highest probability.
  It works best when the relationship between input and output
  is roughly linear.
""")

lr_model = LogisticRegression(max_iter=200)
lr_model.fit(X_train, y_train)
lr_predictions = lr_model.predict(X_test)
lr_accuracy = accuracy_score(y_test, lr_predictions) * 100

print(f"Predicted Labels : {lr_predictions}")
print(f"Actual Labels    : {y_test}")
print(f"Accuracy         : {lr_accuracy:.2f}%")
accuracies["Logistic Regression"] = lr_accuracy

# ===================================================
# ALGORITHM 2: DECISION TREE
# ===================================================
print("\n" + "-" * 60)
print("   ALGORITHM 2: DECISION TREE")
print("-" * 60)
print("""
Description:
  A Decision Tree is a flowchart-like algorithm that splits
  the data into branches based on feature values, just like
  a tree structure. It asks a series of yes/no questions
  about the data and follows the path to reach a final
  decision (class). It is very easy to understand and
  visualize. It can sometimes overfit if the tree grows
  too deep.
""")

dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_predictions = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_predictions) * 100

print(f"Predicted Labels : {dt_predictions}")
print(f"Actual Labels    : {y_test}")
print(f"Accuracy         : {dt_accuracy:.2f}%")
accuracies["Decision Tree"] = dt_accuracy

# ===================================================
# ALGORITHM 3: K-NEAREST NEIGHBORS (KNN)
# ===================================================
print("\n" + "-" * 60)
print("   ALGORITHM 3: K-NEAREST NEIGHBORS (KNN)")
print("-" * 60)
print("""
Description:
  KNN is a simple algorithm that classifies a new data point
  by looking at its K nearest neighbors in the training data
  and taking a majority vote. For example, if K=3 and 2 out
  of 3 nearest neighbors are 'Setosa', the new point is
  classified as 'Setosa'. It does not learn a model, it just
  memorizes the training data and compares at prediction time.
  It is slow for large datasets but very accurate for small ones.
""")

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)
knn_predictions = knn_model.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_predictions) * 100

print(f"Predicted Labels : {knn_predictions}")
print(f"Actual Labels    : {y_test}")
print(f"Accuracy         : {knn_accuracy:.2f}%")
accuracies["KNN"] = knn_accuracy

# ===================================================
# ALGORITHM 4: LINEAR REGRESSION (used as classifier)
# ===================================================
print("\n" + "-" * 60)
print("   ALGORITHM 4: LINEAR REGRESSION")
print("-" * 60)
print("""
Description:
  Linear Regression is originally a regression algorithm used
  to predict continuous numbers (like price or temperature).
  Here we are applying it to classification by rounding its
  output to the nearest class. It tries to fit a straight line
  through the data points to find the best relationship between
  input features and output. It is the simplest algorithm and
  works well when data has a linear pattern.
""")

linreg_model = LinearRegression()
linreg_model.fit(X_train, y_train)
linreg_raw = linreg_model.predict(X_test)
linreg_predictions = np.round(linreg_raw).clip(0, 2).astype(int)
linreg_accuracy = accuracy_score(y_test, linreg_predictions) * 100

print(f"Predicted Labels : {linreg_predictions}")
print(f"Actual Labels    : {y_test}")
print(f"Accuracy         : {linreg_accuracy:.2f}%")
accuracies["Linear Regression"] = linreg_accuracy

# ===================================================
# ALGORITHM 5: K-MEANS CLUSTERING
# ===================================================
print("\n" + "-" * 60)
print("   ALGORITHM 5: K-MEANS CLUSTERING")
print("-" * 60)
print("""
Description:
  K-Means is an unsupervised algorithm, meaning it does NOT
  use the labels (y) during training. It groups the data into
  K clusters based on similarity of features. It finds the
  center of each cluster and assigns each data point to the
  nearest center. Since it assigns its own group numbers,
  we map them to the correct class labels for comparison.
  It is useful when you do not know the categories in advance.
""")

kmeans_model = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_model.fit(X)
kmeans_labels = kmeans_model.labels_

# Map KMeans cluster numbers to actual class labels
mapping = {}
for cluster in range(3):
    mask = kmeans_labels == cluster
    most_common = np.bincount(y[mask]).argmax()
    mapping[cluster] = most_common

kmeans_predictions = np.array([mapping[label] for label in kmeans_labels])
kmeans_accuracy = accuracy_score(y, kmeans_predictions) * 100

print(f"Predicted Labels : {kmeans_predictions[:30]} ...")
print(f"Actual Labels    : {y[:30]} ...")
print(f"Accuracy         : {kmeans_accuracy:.2f}%")
accuracies["K-Means Clustering"] = kmeans_accuracy

# ===================================================
# FINAL COMPARISON
# ===================================================
print("\n" + "=" * 60)
print("           FINAL COMPARISON - ALL ALGORITHMS")
print("=" * 60)
print(f"{'Algorithm':<25} {'Accuracy':>10}")
print("-" * 60)
for algo, acc in accuracies.items():
    bar = "█" * int(acc // 5)
    print(f"{algo:<25} {acc:>7.2f}%  {bar}")

print("-" * 60)
best_algo = max(accuracies, key=accuracies.get)
worst_algo = min(accuracies, key=accuracies.get)
print(f"\n🏆 BEST ALGORITHM  : {best_algo} ({accuracies[best_algo]:.2f}%)")
print(f"⚠️  WORST ALGORITHM : {worst_algo} ({accuracies[worst_algo]:.2f}%)")
print("=" * 60)

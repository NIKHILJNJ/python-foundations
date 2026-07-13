import pandas as pd
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# ===== LOAD DATASET =====
data = load_digits()
df = pd.DataFrame(data.data)
df['digit'] = data.target

print("=" * 60)
print("           DATASET: DIGITS")
print("=" * 60)
print(f"Total Rows    : {df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")
print(f"Classes       : Digits 0 to 9 (handwritten digit images)")
print(f"Each Row      : 64 pixel values of an 8x8 image")
print("\nFirst 10 Rows (first 5 pixels + digit label):")
print("-" * 60)
print(df[[0, 1, 2, 3, 4, 'digit']].head(10).to_string(index=False))
print("=" * 60)

X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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
  Here it predicts which digit (0-9) is shown in the image
  based on the 64 pixel values of each handwritten digit.
""")

lr_model = LogisticRegression(max_iter=10000)
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
  A Decision Tree splits the data into branches based on
  feature values, just like a flowchart. It asks a series
  of yes/no questions about the pixel values of the image
  and follows a path to decide which digit it is (0-9).
  It is very easy to understand and visualize but can
  sometimes overfit if the tree grows too deep.
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
  KNN classifies a new data point by looking at its K nearest
  neighbors in the training data and taking a majority vote.
  For example if K=3 and 2 out of 3 nearest digit images
  look like a 7, the new image is classified as 7.
  It does not learn a model, it just memorizes training data
  and compares at prediction time. Works very well for images.
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
  Linear Regression predicts continuous numbers by fitting
  a straight line through data points. Here we apply it to
  classification by rounding its output to the nearest digit
  between 0 and 9. It finds the best linear relationship
  between the pixel values and the digit label. It is the
  simplest algorithm but struggles with complex image data.
""")

linreg_model = LinearRegression()
linreg_model.fit(X_train, y_train)
linreg_raw = linreg_model.predict(X_test)
linreg_predictions = np.round(linreg_raw).clip(0, 9).astype(int)
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
  K-Means is an unsupervised algorithm that groups data into
  K clusters based on similarity of features without using
  labels during training. It finds the center of each cluster
  and assigns each digit image to the nearest center.
  Since it assigns its own group numbers, we map them to
  the correct digit labels for comparison purposes.
""")

kmeans_model = KMeans(n_clusters=10, random_state=42, n_init=10)
kmeans_model.fit(X)
kmeans_labels = kmeans_model.labels_

mapping = {}
for cluster in range(10):
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

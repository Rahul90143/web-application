import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
df = pd.read_csv('news.csv')
df.columns = ['id', 'title', 'text', 'label']
labels = df['label']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], labels, test_size=0.2, random_state=42)

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf_train = tfidf_vectorizer.fit_transform(X_train)
tfidf_test = tfidf_vectorizer.transform(X_test)

# Initialize classifiers
pac = PassiveAggressiveClassifier(max_iter=50, random_state=42)
dtc = DecisionTreeClassifier(random_state=42)
rfc = RandomForestClassifier(n_estimators=100, random_state=42)

# Voting Classifier (Hard Voting)
voting_clf = VotingClassifier(estimators=[('PAC', pac), ('DTC', dtc), ('RFC', rfc)], voting='hard')

# Fit models and store results
classifiers = {'PAC': pac, 'DTC': dtc, 'RFC': rfc, 'Voting': voting_clf}
accuracy_scores = {}
conf_matrices = {}

for name, clf in classifiers.items():
    clf.fit(tfidf_train, y_train)
    y_pred = clf.predict(tfidf_test)
    accuracy_scores[name] = accuracy_score(y_test, y_pred)
    conf_matrices[name] = confusion_matrix(y_test, y_pred)

# Plot accuracy comparison
plt.figure(figsize=(10, 5))
plt.bar(accuracy_scores.keys(), accuracy_scores.values(), color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Classifiers')
plt.ylabel('Accuracy')
plt.title('Accuracy Comparison of Different Classifiers')
plt.ylim(0, 1)
plt.show()

# Plot confusion matrices
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for i, (name, cm) in enumerate(conf_matrices.items()):
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[i])
    axes[i].set_title(f'Confusion Matrix - {name}')
    axes[i].set_xlabel('Predicted')
    axes[i].set_ylabel('Actual')

plt.tight_layout()
plt.show()

# Save vectorizer and model
with open('tfid.pickle', 'wb') as f:
    pickle.dump(tfidf_vectorizer, f)
with open('model_fakenews.pickle', 'wb') as f:
    pickle.dump(voting_clf, f)

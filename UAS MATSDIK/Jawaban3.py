# 1. Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# 2. Membaca dan mempersiapkan dataset
# Misalkan dataset kita dalam bentuk dictionary untuk contoh ini
data = {
    'nilai_rata_rata': [85, 78, 92, 60, 70, 88, 75, 90, 62, 80],
    'kehadiran': [90, 85, 95, 70, 75, 92, 80, 93, 65, 88],
    'ekstrakurikuler': [2, 1, 3, 0, 1, 2, 1, 3, 0, 2],
    'jam_belajar': [15, 12, 20, 8, 10, 18, 11, 22, 7, 14],
    'kelulusan': ['Lulus', 'Lulus', 'Lulus', 'Tidak Lulus', 'Lulus', 'Lulus', 'Lulus', 'Lulus', 'Tidak Lulus', 'Lulus']
}

df = pd.DataFrame(data)

# Encode target variable
df['kelulusan'] = df['kelulusan'].apply(lambda x: 1 if x == 'Lulus' else 0)

# 3. Membagi data menjadi set pelatihan dan pengujian
X = df.drop('kelulusan', axis=1)
y = df['kelulusan']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Melatih model pohon keputusan
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# 5. Evaluasi model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Classification Report:\n{report}')

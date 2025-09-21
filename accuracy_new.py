import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Daftar sinonim untuk kategori tertentu
synonyms = {
    "HOURS": ["timing",  "hour" ],
    "COURSE": ["course", "branch"],
    "FEE": ["fee"],
    "HOSTEL": ["hostel"],
    "LIBRARY": ["Library","book"],
    "SCHOLARSHIP":["scholarship"],
}

# Dataset awal
original_dataset = [
    ("timing of college", "HOURS"),
    ("what is college timing", "HOURS"),
    ("working days", "HOURS"),
    ("when are your guys open", "HOURS"),
    ("what are your hours", "HOURS"),
    ("hours of operation", "HOURS"),
    ("college timing", "HOURS"),
    ("what about college timing", "HOURS"),
    ("is college open on saturday", "HOURS"),
    ("tell me something about college timing", "HOURS"),
    ("when should i attend college", "HOURS"),
    ("college timing", "HOURS"),
    ("what is my college time", "HOURS"),
    ("timing college", "HOURS"),
    ("list of courses you offered", "COURSE"),
    ("courses offered", "COURSE"),
    ("courses offered in (your university)", "COURSE"),
    ("what are the courses offered in UNI", "COURSE"),
    ("what are branches in UNI", "COURSE"),
    ("can you tell me the courses available in UNI", "COURSE"),
    ("can you tell me the branches available in UNI ", "COURSE"),
    ("computer engineering", "COURSE"),
    ("it","COURSE"),
    ("information technology", "COURSE"),
    ("AI/ML", "COURSE"),
    ("mechanical engineering", "COURSE"),
    ("chemical engineering", "COURSE"),
    ("civil engineering", "COURSE"),
    ("branches", "COURSE"),
    ("courses available at UNI?", "COURSE"),
    ("branches available at your college", "COURSE"),
    ("what are courses at your UNI", "COURSE"),
    ("branches available in UNI", "COURSE"),
    ("computer engineering?", "COURSE"),
    ("computer", "COURSE"),
    ("IT", "COURSE"),
    ("information on fee", "FEE"),
    ("tell me the fee", "FEE"),
    ("college fee", "FEE"),
    ("what is the fee of each semester", "FEE"),
    ("what is fee", "FEE"),
    ("how much is the fees", "FEE"),
    ("fees for first year", "FEE"),
    ("about the fees", "FEE"),
    ("how much is the fees", "FEE"),
    ("fees for non-AC room", "FEE"),
    ("fees for non-AC for girls", "FEE"),
    ("fees per semester", "FEE"),
    ("what is the fee of each year", "FEE"),
    ("what is the fee", "FEE"),
    ("what is the fees of hostel", "HOSTEL"),
    ("fees", "FEE"),
    ("what about the fee", "FEE"),
    ("what is the fees of hostel", "FEE"),
    ("hostel facility", "HOSTEL"),
    ("hostel address", "HOSTEL"),
    ("hostel facilities", "HOSTEL"),
    ("hostel fees", "HOSTEL"),
    ("does college provide hostel", "HOSTEL"),
    ("where is hostel", "HOSTEL"),
    ("do you guys have hostel", "HOSTEL"),
    ("how far is hostel from college", "HOSTEL"),
    ("hostel capacity", "HOSTEL"),
    ("how to get in hostel", "HOSTEL"),
    ("what is hostel address", "HOSTEL"),
    ("where is the hostel", "HOSTEL"),
    ("distance between college and hostel", "HOSTEL"),
    ("distance between hostel and college", "HOSTEL"),
    ("hostel college distance", "HOSTEL"),
    ("what is the fees of hostel", "HOSTEL"),
    ("hostel fees", "HOSTEL"),
    ("hostel", "HOSTEL"),
    ("how big is the hostel", "HOSTEL"),
    ("scholarship","SCHOLARSHIP"),
    ("is scholarship available","SCHOLARSHIP"),
    ("scholarship it", "SCHOLARSHIP"),
    ("scholarship ce", "SCHOLARSHIP"),
    ("scholarship civil", "SCHOLARSHIP"),
    ("scholarship chemical", "SCHOLARSHIP"),
    ("scholarship for computer engineering", "SCHOLARSHIP"),
    ("scholarship for IT engineering", "SCHOLARSHIP"),
    ("scholarship for mechanical engineering", "SCHOLARSHIP"),
    ("scholarship for civil engineering", "SCHOLARSHIP"),
    ("scholarship for chemical engineering", "SCHOLARSHIP"),
    ("IT scholarship", "SCHOLARSHIP"),
    ("mechanical scholarship", "SCHOLARSHIP"),
    ("civil scholarship", "SCHOLARSHIP"),
    ("chemical scholarship", "SCHOLARSHIP"),
    ("automobile scholarship", "SCHOLARSHIP"),
    ("second year scholarship", "SCHOLARSHIP"),
    ("third year scholarship", "SCHOLARSHIP"),
    ("available scholarship", "SCHOLARSHIP"),
    ("first year scholarship", "SCHOLARSHIP"),
    ("fourth scholarship", "SCHOLARSHIP"),
    ("is there any library","LIBRARY"),
    ("library facility", "LIBRARY"),
    ("library facilities", "LIBRARY"),
    ("do you have library", "LIBRARY"),
    ("does the college have library facility", "LIBRARY"),
    ("college library", "LIBRARY"),
    ("books facility", "LIBRARY"),
    ("how many libraries", "LIBRARY"),
    ("where can i find library?", "LIBRARY"),
    ("library", "LIBRARY"),
]

# Menambahkan sinonim ke dalam dataset
dataset = original_dataset.copy()
for category, words in synonyms.items():
    for word in words:
        dataset.append((word, category))

# Fungsi preprocessing
def preprocess_text(text):
    text = text.lower()
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

# Preprocess semua data
preprocessed_texts = [preprocess_text(text) for text, _ in dataset]
labels = [category for _, category in dataset]

# TF-IDF vektorisasi
vectorizer = TfidfVectorizer()
features_vectorized = vectorizer.fit_transform(preprocessed_texts)

# Semua data sebagai data training
X_train = features_vectorized
y_train = labels

# Masukkan nilai k
while True:
    try:
        k = int(input("Masukkan nilai k untuk k-NN: "))
        if k > 0:
            break
        else:
            print("Nilai k harus lebih besar dari 0. Coba lagi.")
    except ValueError:
        print("Input tidak valid. Masukkan nilai integer.")

# Melatih dan menguji K-NN pada data training
knn_classifier = KNeighborsClassifier(n_neighbors=k, metric='cosine')
knn_classifier.fit(X_train, y_train)
y_pred = knn_classifier.predict(X_train)

# Hitung metrik evaluasi
akurasi_manual = sum(1 for pred, actual in zip(y_pred, y_train) if pred == actual) / len(y_train)
precision = precision_score(y_train, y_pred, average='weighted', zero_division=0)
recall = recall_score(y_train, y_pred, average='weighted', zero_division=0)
f1 = f1_score(y_train, y_pred, average='weighted', zero_division=0)

# Tampilkan hasil
print("\nAkurasi :", round(akurasi_manual, 2))
print("Presisi :", round(precision, 2))
print("Recall  :", round(recall, 2))
print("F1-Score:", round(f1, 2))

# Laporan per kelas
print("\nLaporan Klasifikasi per Kelas:\n")
print(classification_report(y_train, y_pred, zero_division=0))
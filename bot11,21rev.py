from flask import Flask, request
import telebot
import nltk
import random
import numpy as np
import string
import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from datetime import datetime

# NLTK download
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# === BOT DAN MODEL SETUP ===
TOKEN = ''
bot = telebot.TeleBot(TOKEN)

# Sinonim
hours_synonyms = ["timing",  "hour" ]
course_synonyms = ["course", "branch"]
fee_synonyms = ["fee"]
hostel_synonyms = ["hostel"]
library_synonyms  = ["library","book"]
scholarship_synonyms =["scholarship"]
# Dataset sederhana
corpus = [
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

# === Preprocessing & Training ===
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def preprocess_text(text):
    text = text.lower()
    text = remove_punctuation(text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

def extract_features(sentence):
    words = preprocess_text(sentence)
    if any (word in hours_synonyms for word in words):
        words.append("HOURS")
    if any (word in course_synonyms for word in words):
        words.append("COURSE")
    if any (word in fee_synonyms for word in words):
         words.append("FEE")
    if any (word in hostel_synonyms for word in words):
         words.append("HOSTEL")
    if any (word in scholarship_synonyms for word in words):
          words.append("SCHOLARSHIP")
    if any (word in library_synonyms for word in words):
          words.append("LIBRARY")
    return ' '.join(words)

texts, labels = zip(*[(extract_features(text), label) for text, label in corpus])
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
y = np.array(labels)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
knn_classifier = KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(X_train, y_train)

responses = {
	"HOURS": ["The college is open from 8 AM to 5 PM, Monday to Saturday."],
	"COURSE": ["Our university offers Information Technology, Computer Engineering, Mechanical Engineering, Chemical Engineering, Civil Engineering, and EXTC Engineering."],
	"FEE": ["For fee details, visit <a target=\"_blank\" href=\"LINK\">here</a>"],
	"HOSTEL": ["For hostel details, visit <a target=\"_blank\" href=\"ADD LINK\">here</a>"],
	"LIBRARY": ["The library is open from 8 AM to 6 PM. For more details, visit <a target=\"_blank\" href=\"ADD LINK\">here</a>"],
	"SCHOLARSHIP": ["Many government scholarships are available. For details, visit <a target=\"_blank\" href=\"ADD LINK\">here</a>."],
}

def chatbot_response(input_text):
    input_text = extract_features(input_text)
    input_vectorized = vectorizer.transform([input_text])
    predicted_category = knn_classifier.predict(input_vectorized)[0]
    return random.choice(responses.get(predicted_category, ["Sorry, I didn't understand."]))

def log_message(user_id, username, message):
    try:
        with open("log.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), user_id, username, message])
    except Exception as e:
        print(f"Error saat menyimpan ke CSV: {e}")

# === FLASK SETUP ===
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Bot is running!", 200

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

# Handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    print(f"Pesan diterima: {message.text}")
    username = message.from_user.username if message.from_user.username else "N/A"
    log_message(message.from_user.id, username, message.text)
    response = chatbot_response(message.text)
    print(f"Respon bot: {response}")
    bot.reply_to(message, response)

# === JALANKAN APP ===
if __name__ == "__main__":
    app.run(debug=True, port=5000)

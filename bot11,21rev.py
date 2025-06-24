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
TOKEN = '7895477673:AAGUc8GpsAKGbeNnvHiSzumEisqMFeuVWsc'
bot = telebot.TeleBot(TOKEN)

# Sinonim
greeting_synonyms = ["hi", "hello", "hey", "anyone", "whatsup"]
farewell_synonyms = ["cya", "goodbye", "bye", "see", "later"]
creator_synonyms = ["creators", "creator", "developers", "developer", "made", "whom", "created", "creators", "designed"]
name_synonyms = ["called"]
hours_synonyms = ["timing", "working", "open", "hours", "operation", "come", "attend"]
course_synonyms = ["courses", "branches"]
fee_synonyms = ["fee", "boys", "girls"]
hostel_synonyms = ["hostel"]
event_synonyms = ["events", "event", "functions"]
document_synonyms = ["documents", "document"]
floor_synonyms    = ["size","campus", "building", "floors","floor","tall"]
syllabus_synonyms = ["syllabus", "lecture","timetable"]
library_synonyms  = ["library","book","books"]
canteen_synonyms  = ["canteen"]
menu_synonyms     =["menu","variety","eat"]
placement_synonyms =["placement", "companies", "average", "package", "recruitment"]
principal_synonyms   =["principal", "principals"]
sem_synonyms         =["exam","dates","schedule","sem"]
admission_synonyms   =["admission", "process"]
scholarship_synonyms =["scholarship"]
collegeintake_synonyms=["max", "seats", "intake", "each branch", "seat"]
random_synonyms=["marry","love"]
vacation_synonyms=["holidays", "starts", "end","vacations","holiday"]
sports_synonyms=["sports","games"]
salutation_synonyms=["thanks","ok","okay"]
ragging_synonyms=["ragging", "antiragging"]
hod_synonyms=["hod","hod name","who is the hod"]

# Dataset sederhana
corpus = [
    ("hi there", "GREETING"),
    ("hello, anyone here?", "GREETING"),
    ("hello", "GREETING"),
    ("heyy","GREETING"),
    ("goodbye","FAREWELL"),
    ("bye","FAREWELL"),
    ("bye for now", "FAREWELL"),
    ("i got to go","FAREWELL"),
    ("goodbye see you later","FAREWELL"),
    ("goodbye see ","FAREWELL"),
    ("see you later","FAREWELL"),
    ("see you","FAREWELL"),
    ("see you later","FAREWELL"),
    ("developers create amazing things", "DEVELOPER"),
    ("creators bring ideas to life", "DEVELOPER"),
    ("what is the name of the developers", "DEVELOPER"),
    ("what is the name of your developers", "DEVELOPER"),
    ("what is the name of your creators", "DEVELOPER" ),
    ("you are made by", "DEVELOPER"),
    ("you are made by whom", "DEVELOPER"),
    ("who created you", "DEVELOPER"),
    ("creators", "DEVELOPER"),
    ("your developers", "DEVELOPER"),    
    ("who designed you", "DEVELOPER"),
    ("who are your developers", "DEVELOPER"),
    ("developers", "DEVELOPER"),
    ("who create you", "DEVELOPER"),
    ("your creators","DEVELOPER"),
    ("do you have a name", "NAMED"),
    ("what should i called you","NAMED"), 
    ("what am i chatting to","NAMED"),
    ("what am i talking to", "NAMED"),
    ("name","NAMED"), 
    ("when is the college open","HOURS"),
    ("what is college timing","HOURS"),
    ("what is the college hours","HOURS"),
    ("when should i attend college","HOURS"),
    ("when should i come to college","HOURS"),    
    ("what are the courses offerd in your college","COURSE"),
    ("courses","COURSE"),
    ("Courses you offer","COURSE"),
    ("branches","COURSE"),
    ("courses available at UNI","COURSE"),
    ("branches available at your college","COURSE"),
    ("what are courses in UNI","COURSE"),
    ("branches available in UNI ","COURSE"),
    ("Computer engineering","COURSE"),
    ("computer","COURSE"),
    ("IT","COURSE"),
    ("can you tell me the branches available in UNI?","COURSE"),
    ("civil engineering","COURSE"),
    ("fees for non-AC room for girls", "FEE"),
    ("fees for non-AC room for boys", "FEE"),
    ("about the fee", "FEE"), 
    ("tell me the fees", "FEE"),  
    ("what is the fee of each year", "FEE"),
    ("what is fees", "FEE"), 
    ("tell me something about the fees ", "FEE"),
    ("What is the fees of hostel", "FEE"),
    ("hostel facilities", "HOSTEL"),
    ("what is the hostel address", "HOSTEL"),
    ("how far hostel from college", "HOSTEL"),
    ("how big is the hostel", "HOSTEL"),
    ("hostel college distance", "HOSTEL"),
    ("Events", "EVENTS"),
    ("list of events organised in college", "EVENTS"),
    ("list of events organised", "EVENTS"),
    ("what are the events", "EVENTS"),
    ("what about events", "EVENTS"),
    ("documents required for admission", "DOCUMENT"),
    ("documents needed at the time of admission", "DOCUMENT"),
    ("what document are required for admission", "DOCUMENT"),
    ("documents  needed for admision", "DOCUMENT"),
    ("documents needed during admission", "DOCUMENT"),
    ("documents needed", "DOCUMENT"),
    ("document to bring", "DOCUMENT"),
    ("documents", "DOCUMENT"),
    ("floors in college?", "FLOOR"),
    ("How many floors does college have", "FLOOR"),
    ("what is the Information Technology syllabus","SYLLABUS"),
    ("Syllabus for IT","SYLLABUS"),
    ("what is timetable","SYLLABUS"),
    ("Library","LIBRARY"),
    ("library books information","LIBRARY"),
    ("library information","LIBRARY"),
    ("does the college have library facility","LIBRARY"),
    ("Does college have canteen","CANTEEN"),
    ("canteen facilities","CANTEEN"),
    ("canteen facility","CANTEEN"),
    ("canteen","CANTEEN"),
    ("is there any canteen","CANTEEN"),
    ("what is there to eat","MENU"),
    ("placement","PLACEMENT"),
    ("about placement","PLACEMENT"),
    ("recruitment","PLACEMENT"),
    ("name of principal","PRINCIPAL"),
    ("principal","PRINCIPAL"),
    ("Where is principals office","PRINCIPAL"),
    ("exam dates", "SEM"),
    ("exam schedule", "SEM"),
    ("when is semester exam", "SEM"),
    ("sem", "SEM"),
    ("when is exam", "SEM"),
    ("Semester exam timetable", "SEM"),
    ("exam timetable", "SEM"),
    ("exam dates", "SEM"),
    ("what is the process of admission","ADMISSION"),
    ("admission","ADMISSION"),
    ("scholarship","SCHOLARSHIP"),
    ("is scholarship available","SCHOLARSHIP"),
    ("fourth year scholarship for mechanical engineering","SCHOLARSHIP"),
    ("What is college intake","COLLEGEINTAKE"),
    ("seats","COLLEGEINTAKE"),
    ("maximum students intake","COLLEGEINTAKE"),
    ("number of seats per branch","COLLEGEINTAKE"),
    ("maximum number of seats","COLLEGEINTAKE"),
    ("how many student are taken in each branch","COLLEGEINTAKE"),
    ("Do you love me","RANDOM"),
    ("I love you","RANDOM"),
    ("Will you marry me","RANDOM"),
    ("holiday list","VACATION"),
    ("Holiday in these year","VACATION"),
    ("about holidays","VACATION"),
    ("When is holidays","VACATION"),
    ("sports and games","SPORTS"),
    ("sports facilities offered","SPORTS"),
    ("Sports activities","SPORTS"),
    ("what is sports available in UNI","SPORTS"),
    ("information about sports","SPORTS"),
    ("sports clubs or teams in UNI","SPORTS"),
    ("okk","SALUTATION"),
    ("nice work","SALUTATION"),
    ("okay","SALUTATION"),
    ("okie","SALUTATION"),
    ("its ok","SALUTATION"),
    ("Good work","SALUTATION"),
    ("ok","SALUTATION"),
    ("ragging","RAGGING"),
    ("is ragging done here","RAGGING"),
    ("does college have any antiragging facility","RAGGING"),
    ("is there any ragging cases","RAGGING"),
    ("antiragging facility","RAGGING"),
    ("ragging against","RAGGING"),
    ("ragging history","RAGGING"),
    ("ragging incidents","RAGGING"),
    ("hod","HOD"),
    ("hod name","HOD"),    
    ("who is the hod","HOD")

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
    if any(word in greeting_synonyms for word in words):
        words.append("GREETING")
    if any(word in farewell_synonyms for word in words):
        words.append("FAREWELL")
    if any(word in creator_synonyms for word in words):
        words.append("DEVELOPER")
    if any (word in name_synonyms for word in words):
        words.append("NAMED")
    if any (word in hours_synonyms for word in words):
        words.append("HOURS")
    if any (word in course_synonyms for word in words):
        words.append("COURSE")
    if any (word in fee_synonyms for word in words):
         words.append("FEE")
    if any (word in hostel_synonyms for word in words):
         words.append("HOSTEL")
    if any (word in event_synonyms for word in words):
         words.append("EVENTS")
    if any (word in document_synonyms for word in words):
         words.append("DOCUMENT")
    if any (word in floor_synonyms for word in words):
         words.append("FLOOR")
    if any (word in syllabus_synonyms for word in words):
         words.append("SYLLABUS")
    if any (word in canteen_synonyms for word in words):
         words.append("CANTEEN")
    if any (word in menu_synonyms for word in words):
          words.append("MENU")
    if any (word in placement_synonyms for word in words):
          words.append("PLACEMENT")
    if any (word in principal_synonyms for word in words):
          words.append("PRINCIPAL")
    if any (word in sem_synonyms for word in words):
          words.append("SEM")
    if any (word in admission_synonyms for word in words):
          words.append("ADMISSION")
    if any (word in scholarship_synonyms for word in words):
          words.append("SCHOLARSHIP")
    if any (word in collegeintake_synonyms for word in words):
          words.append("COLLEGEINTAKE")
    if any (word in random_synonyms for word in words):
          words.append("RANDOM")
    if any (word in sports_synonyms for word in words):
          words.append("SPORTS")
    if any (word in salutation_synonyms for word in words):
          words.append("SALUTATION")
    if any (word in ragging_synonyms for word in words):
          words.append("RAGGING")
    if any (word in hod_synonyms for word in words):
          words.append("HOD")
    return ' '.join(words)

texts, labels = zip(*[(extract_features(text), label) for text, label in corpus])
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
y = np.array(labels)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
knn_classifier = KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(X_train, y_train)

responses = {
    "GREETING": ["Hi there! How can I help you?", "Hello!", "Hi, glad to see you!"],
    "FAREWELL": ["Sad to see you go", "Talk to you later", "Goodbye", "Come back soon"],
    "DEVELOPER": ["College Student."],
	"NAMED": ["You can call me Mind Reader", "I'm Mind Reader", "I am a chatbot"],
	"HOURS": ["The college is open from 8 AM to 5 PM, Monday to Saturday."],
	"NUMBER": ["You can contact at 0215654132"],
	"COURSE": ["Our university offers Information Technology, Computer Engineering, Mechanical Engineering, Chemical Engineering, Civil Engineering, and EXTC Engineering."],
	"FEE": ["For fee details, visit <a target=\"_blank\" href=\"LINK\">here</a>"],
	"LOCATION": ["<a target=\"_blank\" href=\"ADD YOUR GOOGLE MAP LINK HERE\">here</a>"],
	"HOSTEL": ["For hostel details, visit <a target=\"_blank\" href=\"ADD LINK\">here</a>"],
	"EVENTS": ["For event details, visit <a target=\"_blank\" href=\"ADD LINK\">here</a>"],
	"DOCUMENT": ["To know more about required documents, visit <a target=\"_blank\" href=\"ADD LINK\">here</a>"],
	"FLOOR": ["My college has a total of 2 floors."],
	"SYLLABUS": ["To know about the syllabus, visit <a target=\"_blank\" href=\"ADD LINK\">here</a>"],
	"LIBRARY": ["The library is open from 8 AM to 6 PM. For more details, visit <a target=\"_blank\" href=\"ADD LINK\">here</a>"],
	"INFRASTRUCTURE": ["Our university has excellent infrastructure, clean campus, and well-equipped IT labs with high-speed internet."],
	"CANTEEN": ["Our university has a canteen with a variety of food available."],
	"MENU": ["We serve Franky, Locho, Alu-puri, Kachori, Khavsa, Thaali, and many more."],
	"PLACEMENT": ["To know about placement opportunities, visit <a target=\"_blank\" href=\"ADD LINK\">here</a>"],
	"PRINCIPAL": ["XYZ is the college principal. If you need any help, contact your branch HOD first."],
	"ADMISSION": ["Applications can be submitted online through the university's <a target=\"_blank\" href=\"ADD LINK\">website</a>."],
	"SCHOLARSHIP": ["Many government scholarships are available. For details, visit <a target=\"_blank\" href=\"ADD LINK\">here</a>."],
	"FACILITIES": ["Our university provides AC labs, smart classrooms, auditoriums, libraries, and canteens."],
	"SPORTS": ["We provide sports facilities on campus. For more details, visit <a target=\"_blank\" href=\"ADD LINK\">here</a>."],
	"SALUTATION": ["I'm glad I helped you.", "You're welcome!"],
	"TASK": ["I can answer basic to intermediate questions about the college.", "You can ask me anything about the college, and I'll try my best to help."],
	"RAGGING": ["Our college provides a ragging-free environment with strict rules against ragging."],
	"HOD": ["HODs differ for each branch. Please specify your department, e.g., 'HOD IT'."],
	"RANDOM": ["I'm not programmed for this, please ask an appropriate query."],
	"VACATION": ["The academic calendar is given by your class coordinators after you join."],
	"UNIFORM": ["ENTER your own uniform regularly."],
	"COLLEGEINTAKE": ["For IT, Computer and extc 60 per branch and seat may be differ for different department"],
	"SEM": ["Here is the Academic Calendar <a target=\"_blank\" href=\"YOUR ACADEMIC CALENDER\">website</a>"],
	"COMMITTEE":["For the various committe in college contact this number: ADD NUMBER"],

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

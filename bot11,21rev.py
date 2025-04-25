import re
import nltk
import random
import numpy as np
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from telebot import TeleBot

# Pastikan resource NLTK sudah didownload
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Inisialisasi bot Telegram
bot = TeleBot('7895477673:AAGUc8GpsAKGbeNnvHiSzumEisqMFeuVWsc')

# Sinonim kategori
greeting_synonyms = ["hi", "hello", "hey", "anyone", "whatsup"]
farewell_synonyms = ["cya", "goodbye", "bye", "see", "later"]
creator_synonyms = ["creators", "creator", "developers", "developer", "made", "whom", "created", "creators", "designed"]
name_synonyms = ["called"]
hours_synonyms = ["timing", "working", "open", "hours", "operation", "come", "attend"]
number_synonyms = ["info", "contact", "telephone", "phone"]
course_synonyms = ["courses", "branches"]
fee_synonyms = ["fee", "boys", "girls"]
location_synonyms = ["located", "reach"]
hostel_synonyms = ["hostel"]
event_synonyms = ["events", "event", "functions"]
document_synonyms = ["documents", "document"]
floor_synonyms    = ["size","campus", "building", "floors","floor","tall"]
syllabus_synonyms = ["syllabus", "lecture","timetable"]
library_synonyms  = ["book","books","library"]
infrastructure_synonyms   = ["infrastructure"]
canteen_synonyms  = ["cafetaria"]
menu_synonyms     =["menu","variety","eat","canteen"]
placement_synonyms =["placement", "companies", "average", "package", "recruitment"]
ithod_synonyms    =["ithod"]
computerhod_synonyms =["computerhod"]
extchod_synonyms     =["extc"]
principal_synonyms   =["principal"]
sem_synonyms         =["exam","dates","schedule"]
admission_synonyms   =["admission", "process"]
scholarship_synonyms =["scholarship"]
facilities_synonyms =["facilities college provide","College facility","college facilities", "facilities provided"]
collegeintake_synonyms=["max", "seats", "intake", "each branch", "seat"]
uniform_synonyms=["dress","code","uniform","casuals"]
committee_synonyms=["committee"]
random_synonyms=["marry","love"]
swear_synonyms=["stupid", "idiot"]
vacation_synonyms=["holidays", "starts", "end","vacations"]
sports_synonyms=["sports","games"]
salutation_synonyms=["thanks","ok","okay"]
task_synonyms=["help", "use"]
ragging_synonyms=["ragging", "antiragging"]
hod_synonyms=["hod name","who is the hod"]

# Dataset
corpus = [
    ("hi there", "GREETING"),
    ("hello, anyone here?", "GREETING"),
    ("hello", "GREETING"),
    ("heyy","GREETING"),
    ("??? ??? ??", "GREETING"),
    ("cya", "FAREWELL"),
    ("bye bye","FAREWELL"),
    ("see you later","FAREWELL"),
    ("i am leaving","FAREWELL"),
    ("bye","FAREWELL"),
    ("see you later","FAREWELL"),
    ("i am leaving","FAREWELL"),
    ("bye","FAREWELL"),
   ("see you later","FAREWELL"),
    ("i am leaving","FAREWELL"),
    ("bye","FAREWELL"),
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
    ("your name", "NAMED"),
    ("do you have a name", "NAMED"),
    ("what is your name", "NAMED"),
    ("what should i call you","NAMED"),
    ("who are you", "NAMED"),
    ("who is this", "NAMED"),
    ("what am i chatting to","NAMED"),
    ("what am i talking to", "NAMED"),
    ("what are you","NAMED"),
    ("name","NAMED"),    
    ("what is my college time","HOURS"),
    {"timing of college","HOURS"},
    {"what is college timing","HOURS"},
    {"working day","HOURS"},
    {"when are you guys open","HOURS"}, 
    {"what are your hours","HOURS"},
    ("when should i attend college","HOURS"),
    ("college timing","HOURS"),    
    {"hours of operation","HOURS"},
    ("timing college","HOURS"),
    ("what about college timing","HOURS"),
    ("is college open on saturday","HOURS"),
    ("tell something about college time","HOURS"),
    ("when should i come to college","HOURS"),
    {"phone no","NUMBER"},
    {"can i get your phone number","NUMBER"},
    {"how can i call you","NUMBER"},
    {"phone number","NUMBER"},
    {"college phone no?","NUMBER"},
    {"college telephone number?","NUMBER"},
    {"What is your contact no","NUMBER"},
    {"more info","NUMBER"},
    {"how to call you","NUMBER"},
    {"Contact number?","NUMBER"},
    {"college number","NUMBER"},
    {"call","NUMBER"},
    {"how can i call you","NUMBER"},
    {"how to contact college","NUMBER"},
    {"contact info","NUMBER"},
    {"computer engineering","COURSE"},
    {"information technology","COURSE"},
    {"what are courses in UNI?","COURSE"},
    {"can you tell me the courses available in UNI?","COURSE"},
    {"list of courses","COURSE"},
    {"mechanical engineering","COURSE"},
    {"list of courses offered in","COURSE"},
    {"courses you offered in your university","COURSE"},
    {"AI/ML","COURSE"},
    {"chemical engineering","COURSE"},
    {"what are branches in UNI?","COURSE"},
    {"IT","COURSE"},
    {"courses offered","COURSE"},
    {"list of courses offered","COURSE"},
    {"what are the courses in UNI?","COURSE"},
    {"it","COURSE"},
    {"can you tell me the branches available in UNI?","COURSE"},
    {"civil engineering","COURSE"},
    {"fees for non-AC room for girls", "FEE"},
    {"fee", "FEE"},
    {"fees for AC room for girls", "FEE"},
    {"fees for non-AC room", "FEE"},
    {"information on fee", "FEE"},
    {"fees for AC room", "FEE"},
    {"fees for non-AC room for boys", "FEE"},
    {"about the fee", "FEE"}, 
    {"tell me the fee", "FEE"},  
    {"what is the fee of each semester", "FEE"}, 
    {"fees for AC room for boys", "FEE"},
    {"what is fee", "FEE"}, 
    {"college fee", "FEE"}, 
    {"how much is the fees", "FEE"},
    {"fee for first year", "FEE"},
    {"how can i reach  college", "LOCATION"},
    {"address of college","LOCATION"},
    {"college address", "LOCATION"},
    {"where is the college", "LOCATION"}, 
    {"wheres the college", "LOCATION"} ,
    {"college is located at", "LOCATION"} ,
    {"college location", "LOCATION"},
    {"how to reach college", "LOCATION"},
    {"what is the college address", "LOCATION"},
    {"what is the address of college", "LOCATION"},
    {"hostel facilities", "HOSTEL"},
    {"what is the hostel address", "HOSTEL"},
    {"do you guys have hostel", "HOSTEL"},
    {"how to get in hostel", "HOSTEL"},
    {"Does college provide hostel", "HOSTEL"},
    {"what is the hostel fee", "HOSTEL"},
    {"hostel service", "HOSTEL"},
    {"hostel capacity", "HOSTEL"},
    {"distance between college and hostel", "HOSTEL"},
    {"hostel address", "HOSTEL"},
    {"Is there any hostel", "HOSTEL"},
    {"hostel facility", "HOSTEL"},
    {"distance between hostel and college?", "HOSTEL"},
    {"Where is hostel", "HOSTEL"},
    {"hostel fees", "HOSTEL"},
    {"do you have hostel", "HOSTEL"},
    {"hostel location", "HOSTEL"},
    {"Events?", "EVENTS"},
    {"functions", "EVENTS"},
    {"list of events conducted ", "EVENTS"},
    {"what are the events", "EVENTS"},
    {"what about events", "EVENTS"},
    {"list of events", "EVENTS"},
    {"events organised", "EVENTS"},
    {"are there any events held at college", "EVENTS"},
    {"tell me about events", "EVENTS"},
    {"documents required at the time of admission", "DOCUMENT"},
    {"documents needed at the time of admission", "DOCUMENT"},
    {"what documents do i need for admission", "DOCUMENT"},
    {"documents  needed for admision", "DOCUMENT"},
    {"documents needed during admission", "DOCUMENT"},
    {"documents needed", "DOCUMENT"},
    {"document to bring", "DOCUMENT"},
    {"floors in college?", "FLOOR"},
    {"size of campus?", "FLOOR"},
    {"How many floors does college have", "FLOOR"},
    {"size of campus", "FLOOR"},
    {"building size?", "FLOOR"},
    {"building size", "FLOOR"},
    {"what is the Information Technology syllabus","SYLLABUS"},
    {"What is next lecture","SYLLABUS"},
    {"Syllabus for IT","SYLLABUS"},
    {"what is IT syllabus","SYLLABUS"},
    {"timetable","SYLLABUS"},
    {"Where is library","LIBRARY"},
    {"how many libraries","LIBRARY"},
    {"library facilities","LIBRARY"},
    {"college library","LIBRARY"},
    {"do you have library","LIBRARY"},
    {"book facility","LIBRARY"},
    {"is there any library","LIBRARY"},
    {"library facility","LIBRARY"},
    {"where can i get books","LIBRARY"},
    {"does the college have library facility","LIBRARY"},
    {"how is college infrastructure", "INFRASTRUCTURE"},
    {"infrastructure", "INFRASTRUCTURE"},
    {"food facilities","CANTEEN"},
    {"canteen facilities","CANTEEN"},
    {"is there any canteen","CANTEEN"},
    {"is there a cafetaria in college","CANTEEN"},
    {"Does college have canteen","CANTEEN"},
    {"Where is canteen","CANTEEN"},
    {"where is cafetaria","CANTEEN"},
    {"canteen","CANTEEN"},
    {"Food","CANTEEN"},
    {"food menu","MENU"},
    {"food in canteen","MENU"},
    {"whats there on menu","MENU"},
    {"what is available in college canteen","MENU"}, 
    {"what food can we get in college canteen","MENU"},
    {"food variety","MENU"},
    {"Which companies visit in college","PLACEMENT"},
    {"package","PLACEMENT"},
    {"companies visit","PLACEMENT"},
    {"What is average package","PLACEMENT"},
    {"what is college placement","PLACEMENT"},
    {"companies visit","PLACEMENT"},
    {"Who is HOD","ITHOD"},
    {"Where is HOD","ITHOD"},
    {"it hod","ITHOD"},
    {"name of it hod","ITHOD"},
    {"who is computer HOD","COMPUTERHOD"},    
    {"where is computer HOD","COMPUTERHOD"},  
    {"computer HOD","COMPUTERHOD"},  
    {"name of computer HOD","COMPUTERHOD"},
    {"name of extc HOD","EXTCHOD"}, 
    {"who is extc hod","EXTCHOD"},
    {"extc hod","EXTCHOD"},  
    {"where is extc HOD","EXTCHOD"},
    {"what is the name of principal","PRINCIPAL"},
    {"what is the principal name","PRINCIPAL"},
    {"principal name","PRINCIPAL"},
    {"who is college principal","PRINCIPAL"},
    {"exam dates", "SEM"},
    {"exam schedule", "SEM"},
    {"when is semester exam", "SEM"},
    {"sem", "SEM"},
    {"when is exam", "SEM"},
    {"Semester exam timetable", "SEM"},
    {"exam timetable", "SEM"},
    {"exam dates", "SEM"},
    {"what is the process of admission","ADMISSION"},
    {"what is the admission process","ADMISSION"},
    {"How to take admission in your college","ADMISSION"},
    {"what is the process for admission","ADMISSION"},
    {"admission","ADMISSION"},
    {"scholarship","SCHOLARSHIP"},
    {"is scholarship available","SCHOLARSHIP"},
    {"scholarship engineering","SCHOLARSHIP"},
    {"scholarship it","SCHOLARSHIP"},
    {"scholarship ce","SCHOLARSHIP"},
    {"scholarship mechanical","SCHOLARSHIP"},
    {"scholarship civil","SCHOLARSHIP"},
    {"scholarship chemical","SCHOLARSHIP"},
    {"scholarship for AI/ML","SCHOLARSHIP"},
    {"scholarship","SCHOLARSHIP"},
    {"available scholarship","SCHOLARSHIP"},
    {"scholarship for computer engineering","SCHOLARSHIP"},
    {"scholarship for IT engineering","SCHOLARSHIP"},
    {"scholarship for mechanical engineering","SCHOLARSHIP"},
    {"scholarship for civil engineering","SCHOLARSHIP"},
    {"scholarship for chemical engineering","SCHOLARSHIP"},
    {"list of scholarship","SCHOLARSHIP"},
    {"comps scholarship","SCHOLARSHIP"},
    {"IT scholarship","SCHOLARSHIP"},
    {"mechanical scholarship","SCHOLARSHIP"},
    {"civil scholarship","SCHOLARSHIP"},
    {"chemical scholarship","SCHOLARSHIP"},
    {"automobile scholarship","SCHOLARSHIP"},
    {"first year of scholarship","SCHOLARSHIP"},
    {"second year of scholarship","SCHOLARSHIP"},
    {"What facilities college provide","FACILITIES"},
    {"facilities provided","FACILITIES"},
    {"College facility","FACILITIES"},
    {"facilities","FACILITIES"},
    {"What are college facilities","FACILITIES"},
    {"What is college intake","COLLEGEINTAKE"},
    {"seats","COLLEGEINTAKE"},
    {"maximum students intake","COLLEGEINTAKE"},
    {"number of seats per branch","COLLEGEINTAKE"},
    {"max number of students","COLLEGEINTAKE"},
    {"seat allotment","COLLEGEINTAKE"},
    {"college dresscode","UNIFORM"},
    {"do we have to wear uniform","UNIFORM"},
    {"Does college have an uniform","UNIFORM"},
    {"Is there any uniform","UNIFORM"},
    {"uniform","UNIFORM"},
    {"what about uniform","UNIFORM"},
    {"college dresscode","UNIFORM"},
    {"what is the uniform","UNIFORM"},
    {"can we wear casuals","UNIFORM"},
    {"different committee in college","COMMITTEE"},
    {"how many committee are there in college","COMMITTEE"},
    {"committee","COMMITTEE"},
    {"what are the different committe in college","COMMITTEE"},
    {"Give me committee details","COMMITTEE"},
    {"Are there any committee in college","COMMITTEE"},
    {"Do you love me","RANDOM"},
    {"I love you","RANDOM"},
    {"Will you marry me","RANDOM"},
    {"shut up","SWEAR"},
    {"stupid","SWEAR"},
    {"dumb ass","SWEAR"},
    {"asshole","SWEAR"},
    {"hell","SWEAR"},
    {"idiot","SWEAR"},
    {"holidays","VACATION"},
    {"when will semester starts","VACATION"},
    {"when will semester end","VACATION"},
    {"Holiday in these year","VACATION"},
    {"about vacations","VACATION"},
    {"When is vacation","VACATION"},
    {"sports and games","SPORTS"},
    {"give sports details","SPORTS"},
    {"sports infrastructure","SPORTS"},
    {"sports facilities","SPORTS"},
    {"Sports activities","SPORTS"},
    {"please provide sports and games information","SPORTS"},
    {"okk","SALUTATION"},
    {"nice work","SALUTATION"},
    {"good job","SALUTATION"},
    {"Thank You","SALUTATION"},
    {"Thanks","SALUTATION"},
    {"k","SALUTATION"},
    {"okay","SALUTATION"},
    {"okie","SALUTATION"},
    {"well done","SALUTATION"},
    {"thanks for the help","SALUTATION"},
    {"its ok","SALUTATION"},
    {"Good work","SALUTATION"},
    {"ok","SALUTATION"},
    {"what can you do","TASK"},
    {"things you can do","TASK"},
    {"how u can help me","TASK"},
    {"what are the thing you can do","TASK"},
    {"what can u do for me","TASK"},
    {"why i should use you","TASK"},
    {"ragging","RAGGING"},
    {"is ragging pratice active in college","RAGGING"},
    {"does college have any antiragging facility","RAGGING"},
    {"is there any ragging cases","RAGGING"},
    {"antiragging facility","RAGGING"},
    {"ragging juniors","RAGGING"},
    {"ragging history","RAGGING"},
    {"ragging incidents","RAGGING"},
    {"hod","HOD"},
    {"hod name","HOD"},    
    {"who is the hod","HOD"}
]
# Fungsi untuk menghapus tanda baca
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Fungsi preprocessing
def preprocess_text(text):
    text = text.lower()
    text = remove_punctuation(text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

# Fungsi ekstraksi fitur
def extract_features(sentence):
    words = preprocess_text(sentence)
    features = {}
    
    for word in words:
        features[word] = True
        if word in greeting_synonyms:
            features["GREETING"] = True
        if word in farewell_synonyms:
            features["FAREWELL"] = True
        if word in creator_synonyms:
            features["DEVELOPER"] = True
        if word in name_synonyms:
            features["NAMED"] = True
        if word in hours_synonyms:
            features["HOURS"] = True
        if word in number_synonyms:
            features["NUMBER"]= True
        if word in course_synonyms:
            features["COURSE"]= True
        if word in fee_synonyms:
            features["FEE"]= True
        if word in location_synonyms:
            features["LOCATION"]= True
        if word in hostel_synonyms:
            features["HOSTEL"]= True
        if word in event_synonyms:
            features["EVENTS"]= True
        if word in document_synonyms:
            features["DOCUMENT"]= True
        if word in floor_synonyms:
            features["FLOOR"]= True
        if word in syllabus_synonyms:
            features["SYLLABUS"]= True
        if word in library_synonyms:
            features["LIBRARY"]= True
        if word in infrastructure_synonyms:
            features["INFRASTRUCTURE"]= True
        if word in canteen_synonyms:
            features["CANTEEN"]= True
        if word in menu_synonyms:
            features["MENU"]= True
        if word in placement_synonyms:
            features["PLACEMENT"]= True
        if word in ithod_synonyms:
            features["ITHOD"]= True
        if word in computerhod_synonyms:
            features["COMPUTERHOD"]= True
        if word in extchod_synonyms:
            features["EXTCHOD"]= True
        if word in principal_synonyms:
            features["PRINCIPAL"]= True
        if word in sem_synonyms:
            features["SEM"]= True
        if word in admission_synonyms:
            features["ADMISSION"]= True
        if word in scholarship_synonyms:
            features["SCHOLARSHIP"]= True
        if word in facilities_synonyms:
            features["FACILITIES"]= True
        if word in collegeintake_synonyms:
            features["COLLEGEINTAKE"]= True
        if word in uniform_synonyms:
            features["UNIFORM"]= True
        if word in committee_synonyms:
            features["COMMITTEE"]= True
        if word in random_synonyms:
            features["RANDOM"]= True
        if word in swear_synonyms:
            features["SWEAR"]= True
        if word in sports_synonyms:
            features["SPORTS"]= True
        if word in salutation_synonyms:
            features["SALUTATION"]= True
        if word in task_synonyms:
            features["TASK"]= True
        if word in ragging_synonyms:
            features["RAGGING"]= True
        if word in hod_synonyms:
            features["HOD"]= True
    return ' '.join(words)

# Proses dataset
texts, labels = zip(*[(extract_features(text), label) for text, label in corpus])

# Konversi teks ke vektor TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
y = np.array(labels)

# Pembagian data latih dan uji 80:20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi dan pelatihan model KNN
knn_classifier = KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(X_train, y_train)

# Dictionary untuk respons chatbot
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
"ITHOD":["All engineering departments have only one hod XYZ who available on"],
"COMPUTERHOD":["All engineering departments have only one hod XYZ who available on"],
"EXTCHOD":["All engineering departments have only one hod XYZ who available on"],
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
"SWEAR": ["Please use appropriate language.", "Maintaining decency would be appreciated."],
"VACATION": ["The academic calendar is given by your class coordinators after you join."],
"UNIFORM": ["ENTER your own uniform regularly."],
"COLLEGEINTAKE": ["For IT, Computer and extc 60 per branch and seat may be differ for different department"],
"SEM": ["Here is the Academic Calendar <a target=\"_blank\" href=\"YOUR ACADEMIC CALENDER\">website</a>"],
"COMMITTEE":["For the various committe in college contact this number: ADD NUMBER"],
}
# Fungsi chatbot
def chatbot_response(input_text):
    input_text = extract_features(input_text)
    input_vectorized = vectorizer.transform([input_text])
    predicted_category = knn_classifier.predict(input_vectorized)[0]
    
    return random.choice(responses.get(predicted_category, ["Sorry, I didn't understand."]))

# Integrasi dengan bot Telegram
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = chatbot_response(message.text)
    bot.reply_to(message, response)

# Mulai bot
bot.polling()
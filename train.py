import nltk
import numpy as np
import random
import string
import warnings
warnings.filterwarnings("ignore")

data = open('features.txt','r',errors = 'ignore')
data_input = data.read()
data_input = data_input.lower()
nltk.download('punkt')
nltk.download('wordnet')
sent_tokens = nltk.sent_tokenize(data_input)
word_tokens = nltk.word_tokenize(data_input)

sent_tokens[:2]
word_tokens[:5]

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

Greeting_Q = ("hello", "hi", "hey", "sup")
Greeting_A = ["Hey! I'm JHat Jr., Talk to me!", "Hi", "Hey", "Hi there", "Hey there", "Hello"]

Java_Q = ("what is java?","what is java","what is java?","what is java", "java")
Java_Ans = "Java is the high-level, object-oriented, robust, secure programming language, platform-independent, high performance, Multithreaded, and portable programming language."

Java_F = ("features of java","features","java features")
Java_AnsF = ["Features of the Java are \n 1. Simple \n 2. Object-Oriented \n 3. Portable \n 4. Robust \n 5. Dynamic"]

Java_OP = ("java oops concepts", "oops concepts", "java oops", "oops")
Java_AnsOP = ["OOPS Concepts in Java are\n >> Abstraction \n >> Encapsulation \n >> Inheritance \n >> Polymorphism"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in Greeting_Q:
            return random.choice(Greeting_A)

def Java(sentence):
    for word in Java_Q:
        if sentence.lower() == word:
            return Java_Ans

def JavaM(sentence):
    for word in Java_F:
        if sentence.lower() == word:
            return random.choice(Java_AnsF)

def JavaO(sentence):
    for word in Java_OP:
        if sentence.lower() == word:
            return random.choice(Java_AnsOP)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf == 0):
        robo_response = robo_response+"Excuse me, could you repeat the question?"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

# Generating response
def responseone(user_response):
    robo_response=''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf == 0):
        robo_response = robo_response+"Excuse me, could you repeat the question?"
        return robo_response
    else:
        robo_response = robo_response+sent_tokensone[idx]
        return robo_response

def chat(user_response):
    user_response = user_response.lower()
    keyword = "  "
    keywordone = " "
    keywordsecond = " "

    if(user_response != 'bye'):
        if(user_response == 'thanks' or user_response == 'thank you' ):
            input_U = False
            return "You are welcome.."
        elif(JavaM(user_response) != None):
            return JavaM(user_response)
        elif(JavaO(user_response) != None):
            return JavaO(user_response)
        else:
            if(user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(keywordsecond) != -1):
                return responseone(user_response)
                sent_tokensone.remove(user_response)
            elif(greeting(user_response) != None):
                return greeting(user_response)
            elif(Java(user_response) != None):
                return Java(user_response)
            else:
                return response(user_response)
                sent_tokens.remove(user_response)
    else:
        input_U = False
        return "Bye! See you soon!"

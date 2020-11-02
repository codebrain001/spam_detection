import os
import warnings
import nexmo
from flask import Flask, render_template, url_for, request
import pickle
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

from dotenv import load_dotenv
load_dotenv()

API_key = os.getenv("API_key")
API_secret = os.getenv("API_secret")
client = nexmo.Client(key=API_key, secret=API_secret)

warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    """ A POST endpoint that sends an SMS. """

    # Extract the form values:
    to_number = request.form['to_number']
    message = request.form['message']

    # Send the SMS message:
    result = nexmo_client.send_message({
        'from': NEXMO_NUMBER,
        'to': to_number,
        'text': message,
    })

    return render_template('outcome.html', number=to_number, msg=message)

    # # Redirect the user back to the form:
    # return redirect(url_for('index'))


# @app.route('/predict', methods=['POST'])
# def predict():
#     model = pickle.load(open("../model/spam_model.pkl", "rb"))
#     tfidf_model = pickle.load(open("../model/tfidf_model.pkl", "rb"))
#     if request.method == "POST":
#         message = [message]
#         dataset = {'message': message}
#         data = pd.DataFrame(dataset)
#         data["message"] = data["message"].str.replace(
#             r'^.+@[^\.].*\.[a-z]{2,}$', 'emailaddress')
#         data["message"] = data["message"].str.replace(
#             r'^http\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/\S*)?$', 'webaddress')
#         data["message"] = data["message"].str.replace(r'£|\$', 'money-symbol')
#         data["message"] = data["message"].str.replace(
#             r'^\(?[\d]{3}\)?[\s-]?[\d]{3}[\s-]?[\d]{4}$', 'phone-number')
#         data["message"] = data["message"].str.replace(r'\d+(\.\d+)?', 'number')
#         data["message"] = data["message"].str.replace(r'[^\w\d\s]', ' ')
#         data["message"] = data["message"].str.replace(r'\s+', ' ')
#         data["message"] = data["message"].str.replace(r'^\s+|\s*?$', ' ')
#         data["message"] = data["message"].str.lower()

#         stop_words = set(stopwords.words('english'))
#         data["message"] = data["message"].apply(lambda x: ' '.join(
#             term for term in x.split() if term not in stop_words))
#         ss = nltk.SnowballStemmer("english")
#         data["message"] = data["message"].apply(lambda x: ' '.join(ss.stem(term)
#                                                                    for term in x.split()))

#         # tfidf_model = TfidfVectorizer()
#         tfidf_vec = tfidf_model.transform(data["message"])
#         tfidf_data = pd.DataFrame(tfidf_vec.toarray())
#         my_prediction = model.predict(tfidf_data)
#     return render_template('outcome.html', number=to_number)


if __name__ == '__main__':
app.run(debug=True)


# @app.route('/predict', methods=['POST'])
# def predict():
#     model = pickle.load(open("../model/spam_model.pkl", "rb"))
#     tfidf_model = pickle.load(open("../model/tfidf_model.pkl", "rb"))
#     if request.method == "POST":
#         message = request.form["message"]
#         message = [message]
#         dataset = {'message': message}
#         data = pd.DataFrame(dataset)
#         data["message"] = data["message"].str.replace(
#             r'^.+@[^\.].*\.[a-z]{2,}$', 'emailaddress')
#         data["message"] = data["message"].str.replace(
#             r'^http\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/\S*)?$', 'webaddress')
#         data["message"] = data["message"].str.replace(r'£|\$', 'money-symbol')
#         data["message"] = data["message"].str.replace(
#             r'^\(?[\d]{3}\)?[\s-]?[\d]{3}[\s-]?[\d]{4}$', 'phone-number')
#         data["message"] = data["message"].str.replace(r'\d+(\.\d+)?', 'number')
#         data["message"] = data["message"].str.replace(r'[^\w\d\s]', ' ')
#         data["message"] = data["message"].str.replace(r'\s+', ' ')
#         data["message"] = data["message"].str.replace(r'^\s+|\s*?$', ' ')
#         data["message"] = data["message"].str.lower()

#         stop_words = set(stopwords.words('english'))
#         data["message"] = data["message"].apply(lambda x: ' '.join(
#             term for term in x.split() if term not in stop_words))
#         ss = nltk.SnowballStemmer("english")
#         data["message"] = data["message"].apply(lambda x: ' '.join(ss.stem(term)
#                                                                    for term in x.split()))

#         # tfidf_model = TfidfVectorizer()
#         tfidf_vec = tfidf_model.transform(data["message"])
#         tfidf_data = pd.DataFrame(tfidf_vec.toarray())
#         my_prediction = model.predict(tfidf_data)
#     return render_template('result.html', prediction=my_prediction)


# @app.route('/')
# def home():
#     return render_template('home.html')


# @app.route('/predict', methods=['POST'])
# def predict():

#     model = pickle.load(open("../model/spam_model.pkl", "rb"))
#     tfidf_model = pickle.load(open("../model/tfidf_model.pkl", "rb"))
#     if request.method == "POST":
#         message = request.form["message"]
#         message = [message]
#         dataset = {'message': message}
#         data = pd.DataFrame(dataset)
#         data["message"] = data["message"].str.replace(
#             r'^.+@[^\.].*\.[a-z]{2,}$', 'emailaddress')
#         data["message"] = data["message"].str.replace(
#             r'^http\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/\S*)?$', 'webaddress')
#         data["message"] = data["message"].str.replace(r'£|\$', 'money-symbol')
#         data["message"] = data["message"].str.replace(
#             r'^\(?[\d]{3}\)?[\s-]?[\d]{3}[\s-]?[\d]{4}$', 'phone-number')
#         data["message"] = data["message"].str.replace(r'\d+(\.\d+)?', 'number')
#         data["message"] = data["message"].str.replace(r'[^\w\d\s]', ' ')
#         data["message"] = data["message"].str.replace(r'\s+', ' ')
#         data["message"] = data["message"].str.replace(r'^\s+|\s*?$', ' ')
#         data["message"] = data["message"].str.lower()

#         stop_words = set(stopwords.words('english'))
#         data["message"] = data["message"].apply(lambda x: ' '.join(
#             term for term in x.split() if term not in stop_words))
#         ss = nltk.SnowballStemmer("english")
#         data["message"] = data["message"].apply(lambda x: ' '.join(ss.stem(term)
#                                                                    for term in x.split()))
#         # tfidf_model = TfidfVectorizer()
#         tfidf_vec = tfidf_model.transform(data["message"])
#         tfidf_data = pd.DataFrame(tfidf_vec.toarray())
#         my_prediction = model.predict(tfidf_data)
#     return render_template('result.html', prediction=my_prediction)

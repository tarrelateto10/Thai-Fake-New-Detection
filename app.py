from flask import Flask, request, jsonify, render_template
import joblib
from pythainlp.tokenize import word_tokenize

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load('./model/fake_news_model.pkl')
vectorizer = joblib.load('./model/vectorizer.pkl')

def preprocess_text(text):
    tokens = word_tokenize(text, engine='newmm')
    return ' '.join(tokens)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form['text']
    preprocessed_text = preprocess_text(data)
    transformed_text = vectorizer.transform([preprocessed_text])
    prediction = model.predict(transformed_text)
    if prediction[0] == 1:
        result = 'Real'
    else:
        result = "Fake"
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)

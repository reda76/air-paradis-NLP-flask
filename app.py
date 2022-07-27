from flask import Flask, render_template, request
from model import predict

app = Flask('Twitter Sentiment Analysis')

@app.route('/')
@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        user_input = request.form["user_tweet"]
        label = predict(user_input)
        return render_template('predictform.html', prediction_text = label)
    return render_template('predictform.html')

if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, request
import os

app = Flask(__name__)

picFolder = os.path.join('static','pics')
app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/")
def home():
    return render_template('page1.html')

@app.route("/", methods=["POST"])
def recv():
    word = request.form[" "]
    with open('input.txt', 'w') as f:
        f.write(word)
    pic = os.path.join(app.config['UPLOAD_FOLDER'], 'wordcloud.png')
    return render_template("page2.html", user_image = pic)

if __name__ == "__main__":
    app.run(debug=True)
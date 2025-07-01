from flask import Flask, render_template
import datetime

app=Flask(__name__)

@app.route("/")
def home():
    today = datetime.datetime.now().strftime('%A')
    return render_template("index.html",todya=today)

if __name__=='__main__':
    app.run(debug=True)
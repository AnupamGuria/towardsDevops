from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route("/")
def home():
    return "this is home"


@app.route("/submit",methods=['post'])
def submit():
    data = request.get_json()  # <-- parses JSON body
    #return jsonify(data)
    return data

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

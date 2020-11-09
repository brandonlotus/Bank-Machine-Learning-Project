import joblib

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bank')
def bank():
    return render_template('bank.html')

@app.route('/result', methods=['POST'])
def hasil():
    if request.method == 'POST':
        input = request.form
        cs = float(input['CreditScore'])
        gd = float(input['Gender'])
        ag = float(input['Age'])
        tn = float(input['Tenure'])
        bl = float(input['Balance'])
        np = float(input['NumOfProducts'])
        cc = float(input['HasCrCard'])
        mb = float(input['IsActiveMember'])
        es = float(input['EstimatedSalary'])
        fr = float(input['Geography_France'])
        gr = float(input['Geography_Germany'])
        sp = float(input['Geography_Spain'])  
        pred = model.predict([[cs,gd,ag,tn,bl,np,cc,mb,es,fr,gr,sp]])[0]

    return render_template('hasil.html', data = input, prediksi = pred)

if __name__ == "__main__":
    model = joblib.load('ModelBank')
    app.run(debug=True)
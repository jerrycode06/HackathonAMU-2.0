from flask import Flask, render_template, request, send_file, redirect
import pickle

# Create Flask app load app.config
app = Flask(__name__)


# Open file, where data is stored
file = open('model.pkl', 'rb')
model = pickle.load(file)
# clf = model[0] when feature scaling is in effect
# sc_X = model[1]
file.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check', methods = ['GET', 'POST'])
def check():
    if request.method == 'POST':
        dictData = request.form
        fever = int(dictData['fever'])
        age = int(dictData['age'])
        bodyPain = int(dictData['bodyPain'])
        runnyNose = int(dictData['runnyNose'])
        diffBreath = int(dictData['diffBreath'])

        features = [fever, age, bodyPain, runnyNose, diffBreath]
        # infProb = clf.predict_proba(sc_X.transform([inputFeatures]))[0][1] when feature scaling is in effect
        prob = model.predict_proba([features])[0][1]

        return render_template('view.html', prob = round(prob*100))
    return render_template('check.html')


@app.route('/map')
def view():
    return render_template('map.html')


@app.route('/notify')
def notify():
    return render_template('notification.html')

@app.route('/down')
def download():
    path = 'Notification_System/Covid_Notification_System.zip'

    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
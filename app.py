from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('Model.pkl', 'rb'))

# decorator


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST','GET'])
def predict():
    age = request.form.get('age')
    sex = request.form.get('sex')
    bmi = request.form.get('bmi')
    children = request.form.get('children')
    smoker = request.form.get('smoker')
    region = request.form.get('region')
    input = [[int(age), int(sex), float(bmi), int(children), int(smoker), int(region)]]
    print(input)
    preds = model.predict(input)
    print(preds)
    return render_template("index.html", Pred="Your estimated expense is ₹ {}/-".format(round(preds[0],2)))


if __name__ == "__main__":
    app.run(debug=True, port=5000)

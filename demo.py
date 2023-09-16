from flask import Flask, render_template, request
import pickle

# app = Flask(__name__)

model = pickle.load(open('Model.pkl', 'rb'))

print(model.predict([[12, 1, 12.12, 2, 1, 1]]))
'''if __name__ == "__main__":
    app.run(debug=True, port=5000)'''

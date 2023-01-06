from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.predict(final)
    print(prediction)
    output = '{0:.{1}f}'.format(prediction[0][0], 2)
    output2 = '{0:.{1}f}'.format(prediction[0][1], 2)
    # output2 = '{0:.{1}f}'.format(prediction2[0][1], 2)

    return render_template('index.html', pred='Required Step count is :  {}'.format(output), pred2='Required Calorie Count is : {}'.format(output2), bhai="kuch karna hain iska ab?")
    # return render_template('index.html', pred2='Required Step count is :  {}'.format(output2), bhai="kuch karna hain iska ab?")



if __name__ == '__main__':
    app.run(debug=True)

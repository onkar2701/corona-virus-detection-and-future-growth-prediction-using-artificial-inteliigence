import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/predict',methods=['POST'])
def predict():

    '''int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features) '''
    #output = round(prediction[2], 6)
    model = pickle.load(open('model.pkl', 'rb'))
    # print(request.args.get('trachea'))
    #
    # print(request.args.get('swab'))

    val1=float(request.form['trachea'])
    val2=float(request.form['swab'])
    query=[[val1,val2]]
    # query = [[float(request.form['trachea','swab'])]]

    # X_query = model.transform(query)
    sal = model.predict(query)
    #print(sal)
    return render_template('input.html', prediction_text='Coronavirus detection is {}'.format(sal))


if __name__ == "__main__":
    app.run(debug=True)
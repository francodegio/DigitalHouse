import pickle
import numpy as np
from flask import Flask, jsonify, request
import pandas
#from sklearn.ensemble import ExtraTreesClassifier 
#from sklearn.feature_extraction.text import TfidVectorizer
#import os

with open('/var/www/pkls/model.pkl', 'rb') as modelpickled:    
    model = pickle.load(modelpickled)

with open('/var/www/pkls/vectorizer.pkl', 'rb') as vectorizerPickle:    
    vectorizer = pickle.load(vectorizerPickle)


app = Flask('Predictor')


#with open('/var/www/pkls/model_columns.pkl', 'rb') as columnspickled:    
#    model_columns = pickle.load(columnspickled)

#def add_missing_dummy_columns( d, columns ):
#    missing_cols = set( columns ) - set( d.columns )
#    for c in missing_cols:
#        d[c] = 0
#def fix_columns( d, columns ):  
#    add_missing_dummy_columns( d, columns )
#    # make sure we have all the columns we need
#    assert( set( columns ) - set( d.columns ) == set())
#    extra_cols = set( d.columns ) - set( columns )
#    if extra_cols:
#        print "extra columns:", extra_cols
#    d = d[ columns ]
#    return d

@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    X = [data["text"]]
    vect_data = vectorizer.transform(X)
    output = model.predict(vect_data)
    prediction = str(output[0])
    output = {'prediction': prediction}
    response = jsonify(output)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
@app.route('/predict_proba',methods=['POST'])
def predict_proba():
    data = request.get_json(force=True)
    X = [data["text"]]
    vect_data = vectorizer.transform(X)
    output = model.predict_proba(vect_data)
    prediction = str(output[0])
    output = {'prediction': prediction}
    response = jsonify(output)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#run(host='localhost', port=8080, debug=True, reloader=True)
app.run(host='fakenews_py', port=8080)

# curl -H "Content-Type: application/json" -X GET -d '{"text":"news"}' http://localhost:8080/predict_proba
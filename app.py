import flask
import pickle
import pandas as pd
from joblib import load

# Load the saved logistic regression model
#model = load('model/Model1.joblib')

with open(f'model/Model1.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
       return(flask.render_template('index.html')) 
    if flask.request.method == 'POST':
       fo = flask.request.form['fo']
       fd = flask.request.form['fd']
       mon = flask.request.form['mon']
       day = flask.request.form['day']
       AET = 0
       AT = 0
       CRSET = 0
       C = 0
       DOW = 0
       DAID = 0
       Dist = 0
       Div = 0
       OS = ''
       P = 0
       W = ''
       S = ''
       input_variables = pd.DataFrame([[fo,fd,C,Div,AT,CRSET,AET,Dist,mon,day,DOW,OS,DAID,W,S,P]],columns=['Origin','Dest','Cancelled','Diverted','AirTime','CRSElapsedTime','ActualElapsedTime','Distance','Month','DayofMonth','DayOfWeek','OriginState','DestAirportID','WeatherType','Severity','Precipitation'])
       prediction = model.predict(input_variables)[0]
       return flask.render_template('index.html',original_input={'Origin':fo,'Dest':fd,'Month':mon,'DayofMonth':day},result=prediction)
       
if __name__ == '__main__':
   app.run()

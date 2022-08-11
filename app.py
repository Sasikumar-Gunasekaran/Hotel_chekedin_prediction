from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import pandas as pd
from xgboost import XGBClassifier

#import tensorflow as tf
#import keras   
#from keras.models import load_model


app = Flask(__name__)

model = pickle.load(open('XGB.pkl', 'rb'))

#model = load_model('hotel.h5')

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')





@app.route("/predict", methods = ["GET", "POST"])
def predict():
    
    if request.method == 'POST':
      Age=float(request.form['Age'])
      DaysSinceCreation=float(request.form['DaysSinceCreation'])

      AverageLeadTime = float(request.form['AverageLeadTime'])
      LodgingRevenue = float(request.form['LodgingRevenue'])
      OtherRevenue    = float(request.form['OtherRevenue'])
      BookingsCanceled = float(request.form['BookingsCanceled'])
      BookingsNoShowed = float(request.form['BookingsNoShowed'])
      BookingsCheckedIn    = float(request.form['BookingsCheckedIn'])
      PersonsNights = float(request.form['PersonsNights'])
      RoomNights = float(request.form['RoomNights'])
      DistributionChannel = request.form['DistributionChannel']
      if (DistributionChannel == 'Corporate'):
          DistributionChannel = 0
      elif(DistributionChannel == 'Direct'):
           DistributionChannel = 1
      elif(DistributionChannel == 'Electronic Distribution'):
           DistributionChannel = 2
      else:
           DistributionChannel = 3
      MarketSegment    = request.form['MarketSegment']
      if (MarketSegment == 'Aviation'):
          MarketSegment = 0
      elif(MarketSegment == 'Complementary'):
           MarketSegment = 1
      elif(MarketSegment == 'Corporate'):
            MarketSegment = 2
      elif(MarketSegment == 'Groups'):
            MarketSegment = 3
      elif(MarketSegment == 'Direct'):
            MarketSegment = 4
      elif(MarketSegment == 'Travel Agent/Operator'):
           MarketSegment = 5
      else:
           MarketSegment = 6
      SRHighFloor = float(request.form['SRHighFloor'])
      SRLowFloor = float(request.form['SRLowFloor'])
      SRAccessibleRoom    = float(request.form['SRAccessibleRoom'])
      SRMediumFloor = float(request.form['SRMediumFloor'])
      SRBathtub = float(request.form['SRBathtub'])
      SRShower    = float(request.form['SRShower'])
      SRCrib = float(request.form['SRCrib'])
      SRKingSizeBed    = float(request.form['SRKingSizeBed'])
      SRTwinBed = float(request.form['SRTwinBed'])
      SRNearElevator = float(request.form['SRNearElevator'])
      SRAwayFromElevator = float(request.form['SRAwayFromElevator'])
      SRNoAlcoholInMiniBar    = float(request.form['SRNoAlcoholInMiniBar'])
      SRQuietRoom = float(request.form['SRQuietRoom'])       
      prediction = model.predict(
       	[[Age, DaysSinceCreation, AverageLeadTime, LodgingRevenue,
           OtherRevenue,BookingsCanceled,BookingsNoShowed,
           BookingsCheckedIn,PersonsNights,RoomNights,
            DistributionChannel,MarketSegment, SRHighFloor, SRLowFloor,
            SRAccessibleRoom, SRMediumFloor, SRBathtub, SRShower, SRCrib,
            SRKingSizeBed, SRTwinBed, SRNearElevator, SRAwayFromElevator,
            SRNoAlcoholInMiniBar, SRQuietRoom]])
      Output=prediction 
      if Output == 0:
            return render_template('index.html', prediction_texts=" Sorry Wont Checked")
      else :
            return render_template('index.html', prediction_text=" Will Be CheckedIn ")
   


if __name__ == "__main__":
     app.run(debug=True)

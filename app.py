from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import pandas as pd
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
      BookingsCanceled = int(request.form['BookingsCanceled'])
      BookingsNoShowed = int(request.form['BookingsNoShowed'])
      BookingsCheckedIn    = int(request.form['BookingsCheckedIn'])
      PersonsNights = int(request.form['PersonsNights'])
      RoomNights = int(request.form['RoomNights'])
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
      SRHighFloor = int(request.form['SRHighFloor'])
      SRLowFloor = int(request.form['SRLowFloor'])
      SRAccessibleRoom    = int(request.form['SRAccessibleRoom'])
      SRMediumFloor = int(request.form['SRMediumFloor'])
      SRBathtub = int(request.form['SRBathtub'])
      SRShower    = int(request.form['SRShower'])
      SRCrib = int(request.form['SRCrib'])
      SRLowFloor = int(request.form['SRLowFloor'])
      SRKingSizeBed    = int(request.form['SRKingSizeBed'])
      SRTwinBed = int(request.form['SRTwinBed'])
      SRNearElevator = int(request.form['SRNearElevator'])
      SRAwayFromElevator = int(request.form['SRAwayFromElevator'])
      SRNoAlcoholInMiniBar    = int(request.form['SRNoAlcoholInMiniBar'])
      SRQuietRoom = int(request.form['SRQuietRoom'])       
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

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "thisisthesecretkey"

@app.route('/')
def index():
  flash("What's My Race Pace?")
  return render_template('index.html')

@app.route('/MyRacePace', methods=["POST", "GET"])
def get_race_pace():


    distance = float(request.form['distance'])
    hour = int(request.form['hour'])
    minutes = int(request.form['minutes'])
    seconds = int(request.form['seconds'])

    pace_raw = ((hour*60)+minutes+(seconds/60))/distance
    pace_minutes = int(pace_raw)
    
    #get digits after decimal from pace_raw
    pace_seconds_dec = '0.'+str(pace_raw).split('.')[1]
    #convert decimal to seconds
    pace_seconds= float(pace_seconds_dec)*60
    #add leading 0 to single-digit seconds to ensure that result is always 2 characters
    pace_seconds_padded = str(int(pace_seconds)).rjust(2, '0')

    race_pace = str(pace_minutes) + ":" + str(pace_seconds_padded)
    
    flash("My Race Pace = " + race_pace)
    
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)












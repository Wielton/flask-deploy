from flask import Flask, request, jsonify
from flask_cors import CORS
import sys

app = Flask(__name__)


tweets = [
    "afadgzdgadgdfg",
    "aghkjkjzsdgklj k ojsdgf oSDfksnfgkj",
    "lksdf ogf oaihjf the sdkjfopi  jppihjef",
    "ujhdfgpio najnfo oif",
    "opihjadfg knsf jsefpknpef okspefolkps",
    
]

@app.get("/api/tweets")
def tweets_get():
    args = request.args
    #tweetId
    tweet_id = int(args.get('tweetId')) # Convert to INT to iterate through the indexes of the array
    if tweet_id == None:
        return jsonify(tweets), 200
    else:
        return jsonify(tweets[tweet_id]), 200
    
if (len(sys.argv) > 1):
    mode = sys.argv[1]
else:
    print("No mode argument: testing | production")
    exit()    
    

if mode == "testing":
    CORS(app)    # Only want CORS on testing servers
    app.run(debug=True)
elif mode == "production":
    import bjoern
    bjoern.run(app, "0.0.0", 5000)
    print('Running in development mode!')
else:
    print("Invalid mode.  Must be testing or production")
    
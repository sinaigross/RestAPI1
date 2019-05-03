import play_scraper
import json

from flask import Flask, request
app = Flask(__name__)

class ScraperResult:
  def __init__(self, title, iconUrl, developerEmail):
    self.title = title
    self.iconUrl = iconUrl
    self.developerEmail = developerEmail

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/getapp")
def getapp():
    appId = request.args.get('appId', None)
    try:
        x = play_scraper.details(appId)
        res = ScraperResult(x.get('title'), x.get('icon'), x.get('developer_email'))
    except:
        res = ScraperResult(None, None, None)

    return json.dumps(res.__dict__);

from flask import Flask, render_template
from threading import Thread
app = Flask(__name__)

@app.route('/')
def home():
  return "i'm alive"

def run():
  app.run(host='almight-bot-jinlover.koyeb.app/', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
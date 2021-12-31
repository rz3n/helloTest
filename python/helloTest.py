# from: https://dev.to/seattledataguy/building-your-first-website-with-flask-part-1-hello-world-and-beyond-53ik

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
  return ('Its working!' +
          '<br>python')

if __name__ == '__main__':
  app.run(host='0.0.0.0')

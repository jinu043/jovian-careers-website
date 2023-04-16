from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell_world():
  return "Hello Learners!!"

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
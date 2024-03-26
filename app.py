from flask import Flask, jsonify, render_template, jsonify

app = Flask(__name__)

Fruits = [
  {
    'id': 1,
    'name': 'Apple',
    'price': 'R.20.00',
  },
  {
    'id': 2,
    'name': 'Banana',
    'price': 'R.35.00',
  },
  {
    'id': 3,
    'name': 'Mango',
    'price': 'R.50.00',
  },
  {
    'id': 4,
    'name': 'Pear',
    'price': 'R.25.50',
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html', fruits=Fruits)

@app.route("/api/fruits")
def list_fruits():
  return jsonify(Fruits)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
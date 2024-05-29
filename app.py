from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 200'
}, {
    'id': 2,
    'title': 'BS',
    'location': 'Delhi, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 3,
    'title': 'DS',
    'location': 'UP, India',
    'salary': 'Rs. 100,000'
}]


@app.route("/")
def book():
    return render_template('booking.html')


@app.route("/trains")
def list():
    return render_template('trains.html', jobs=JOBS)


@app.route('/api/listing')
def listjson():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

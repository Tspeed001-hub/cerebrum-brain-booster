from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_time():
    current_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'current_time': current_time})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
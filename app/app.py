
from datetime import datetime

from flask import Flask, render_template

from redis import StrictRedis

app = Flask(__name__)
redis = StrictRedis(host='backend', port=6379)


@app.route('/')
def home():
    redis.lpush('times', datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z'))
    return render_template('index.html', title='Home',
                           times=redis.lrange('times', 0, -1))


if __name__ == '__main__':
    app.run(host='0.0.0.0')

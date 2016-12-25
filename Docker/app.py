from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Welcome to the tutorial titled "Kong with Kubernetes on AWS" . This page has been visted  %s times.\n' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

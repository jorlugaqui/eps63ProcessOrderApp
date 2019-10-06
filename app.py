import json
import logging
import requests

from flask import Flask, request

logger = logging.getLogger()
logger.setLevel(logging.INFO)
app = Flask(__name__)

@app.route('/process_order', methods = ['GET', 'POST'])
def process_order():
    js = None
    try:
        js = json.loads(request.data)
    except Exception as e:
        pass

    hdr = request.headers.get('X-Amz-Sns-Message-Type')
    # subscribe to the SNS topic
    if hdr == 'SubscriptionConfirmation' and 'SubscribeURL' in js:
        requests.get(js['SubscribeURL'])
    
    logger.info(js)
    
    return 'processed'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
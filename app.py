import json

from flask import Flask, Response, request

app = Flask(__name__)


@app.route("/")
def hello():
    payload = request.args.get('payload')
    print(payload)
    data = [{'name': 'rideOS', 'logo': 'logo', 'link': 'https://rideos.ai', 'keywords': ['car']},
            {'name': 'Dashblock', 'logo': 'logo', 'link': 'https://dashblock.com',
                'keywords': ['api', 'webscrapper']},
            {'name': 'Netlify', 'logo': 'logo', 'link': 'https://www.netlify.com/', 'keywords': []}]
    return Response(json.dumps(data),  mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)

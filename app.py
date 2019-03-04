from flask import Flask, request, jsonify, render_template
import random
import string

app = Flask(__name__)

url_mapping = {}


def generate_short_url():
    return "https://www.koble.jobs/"+''.join(random.choices(string.ascii_letters + string.digits, k=7)) #7 tilfeldige bokstaver/tall
# kanskje legge inn ^ som en egen variabel - lettere å endre senere

def get_long_url(url):
    return url_mapping[url]


def create_response_object(short_url, long_url):
    response = {"shortUrl": short_url, "longUrl": long_url}
    return jsonify(response)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/url', methods=['POST'])
def shorten_url():
    short_url = generate_short_url()
    long_url = request.get_json()["longUrl"]
    url_mapping[short_url] = long_url
    return create_response_object(short_url, long_url)


@app.route('/url', methods=['GET'])
def expand_url():
    short_url = request.args.get('shortUrl')
    long_url = get_long_url(short_url)
    return create_response_object(short_url, long_url)


if __name__ == '__main__':
    app.run(debug=True, port=3000)

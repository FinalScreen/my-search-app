from flask import Flask, request, jsonify
from flask_cors import CORS
from scraping_scripts import scrape_imdb_movie, scrape_espn

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (e.g., from Wix)

@app.route('/')
def home():
    return "Hello from the Universal Scraper!"

@app.route('/search/movies', methods=['GET'])
def search_movies():
    # Example usage: /search/movies?q=Avengers
    query = request.args.get('q', '')
    data = scrape_imdb_movie(query)
    return jsonify(data)

@app.route('/search/sports', methods=['GET'])
def search_sports():
    # Example usage: /search/sports?q=Man+Utd
    query = request.args.get('q', '')
    data = scrape_espn(query)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
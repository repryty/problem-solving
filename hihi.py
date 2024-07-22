from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/gemini/api/v1/<endpoint>', methods=['GET'])
def gemini_api(endpoint):
    # Replace 'YOUR_API_KEY' and 'YOUR_API_SECRET' with your actual Gemini API credentials
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    
    # Construct the Gemini API URL
    url = f'https://api.gemini.com/v1/{endpoint}'
    
    # Make a request to the Gemini API
    response = requests.get(url, auth=(api_key, api_secret))
    
    # Return the response as JSON
    return jsonify(response.json())

if __name__ == '__main__':
    app.run()
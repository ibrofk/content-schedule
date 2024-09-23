from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Airtable API endpoint
AIRTABLE_URL = "https://api.airtable.com/v0/appHr083j1Ui9XXlC/tblpW42tdZbAlZx3e"

# Load your API key from environment variables
AIRTABLE_API_KEY = os.environ.get('AIRTABLE_API_KEY')
# Token = pat83vhURClb1uWX1.632bf9103ec3ebc3154724c86bbb9f843e98044ebcd49d9c15087b69b25357e1
# Check that the API key is available
if not AIRTABLE_API_KEY:
  raise ValueError("AIRTABLE_API_KEY not set in environment variables")

@app.route('/create-content-schedule', methods=['POST'])
def create_content_schedule():
  data = request.get_json()
  if not data:
      return jsonify({'error': 'Invalid JSON data received'}), 400

  headers = {
      "Authorization": f"Bearer {AIRTABLE_API_KEY}",
      "Content-Type": "application/json"
  }

  # Send POST request to Airtable API
  response = requests.post(AIRTABLE_URL, headers=headers, json=data)

  if response.status_code == 200 or response.status_code == 201:
      return jsonify(response.json()), response.status_code
  else:
      return jsonify({
          'error': 'Failed to create record',
          'status_code': response.status_code,
          'details': response.json()
      }), response.status_code

if __name__ == '__main__':
  app.run(debug=True)
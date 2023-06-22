# Store Finder - Seckin Unver

This is a sample Store Finder for Jumbo Supermarkets. This API gives you the nearest Jumbo stores near the provided location.

## Useful Links

- [Github repository](https://github.com/unverseckin/Store-Finder)
- [Live demo](https://seckinunver.pythonanywhere.com)

## API Documentation

### API Endpoint

The API exposes the following endpoint:

#### Get Nearest Stores

- Endpoint: `/store-finder`
- Method: `GET`
- Description: Returns the nearest Jumbo stores based on the provided location.
- Parameters:
  - `latitude` (query parameter): Latitude of the user location (required).
  - `longitude` (query parameter): Longitude of the user location (required).
- Response:
  - Status Code: `200` (Successful operation)
  - Status Code: `400` (Invalid request parameters)

## Installation

To run the Flask API locally, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/unverseckin/Store-Finder.git

2. Install the required dependencies:
   ```shell
   pip install -r requirements.txt

3. Start the Flask server:
   ```shell
   python store_finder_app.py
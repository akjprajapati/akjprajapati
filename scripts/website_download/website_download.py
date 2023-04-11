import os
import requests

def download_website(url, output_dir):
    # Make a GET request to the URL
    response = requests.get(url)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Save the HTML content to a file
    output_file = os.path.join(output_dir, 'index.html')
    with open(output_file, 'w') as f:
        f.write(response.text)

# Example usage
url = 'https://www.stephanemaarek.com/'
output_dir = 'stephanemaarek_com'
download_website(url, output_dir)


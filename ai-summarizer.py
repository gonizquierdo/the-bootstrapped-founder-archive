import requests
import os

# load env
from dotenv import load_dotenv
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer {HUGGINGFACE_TOKEN}}".format(os.environ["HUGGINGFACE_TOKEN"])}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

# Iterate over the files in the out directory
for file in os.listdir('out'):
    # Check if the file is already summarized and skip it
    if os.path.exists('out_summarized/' + file):
        continue

    # Open the file
    with open('out/' + file, 'r', encoding='utf-8') as f:
        text = f.read()
        
        # Query the API
        output = query({
            "inputs": text,
        })
        print(output)

        # Save the summary to a file in the out_summarized dir with the same name as the original file
        with open('out_summarized/' + file, 'w', encoding='utf-8') as f:
            f.write(output[0]['summary_text'])


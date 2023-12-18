import json
import os
from datetime import date, datetime
import requests
from shutil import copyfile

QUESTION_MAPPING = {
    "Date": "What is the current date? (YYYY-MM-DD)",
    "Full Name": "What is your full name?",
    "Current Occupation": "What is your current occupation?",
    "Current Residence": "Where do you currently live?",
    "Place of Birth": "Where were you born?",
    "Current favourite song": "What is your current favorite song?",
    "Latest City Visited": "Which city did you visit last?",
    "Proof": "Provide proof (add an image here):",
    "Newest project": "What is your newest project?",
    "Current favourite object": "What is your current favorite object?",
    "Latest obsessions": "Provide your latest obsessions:",
}

MEDIA_DIR = 'about/media'
storage_file_name = "about/utilities/about_updates.json"

def collect_data():
    answers = {}

    # Ask for the date
    answers["Date"] = input(f"{QUESTION_MAPPING['Date']} ")

    # Automatically record 'Raghav Thakar' for 'Full Name'
    answers['Full Name'] = 'Raghav Thakar'

    # Automatically record 'Delhi, India' for 'Place of Birth'
    answers['Place of Birth'] = 'Delhi, India'

    for shorthand, question in QUESTION_MAPPING.items():
        # Skip asking for 'Date' since we already asked for it
        if shorthand != "Date":
            # Skip automatic recording for 'Full Name' and 'Place of Birth'
            if shorthand not in answers:
                answer = input(f"{question} ")

                # Handle 'Proof' question and get the saved image path
                if shorthand == 'Proof':
                    proof_path = handle_proof(answer)
                    answers[shorthand] = proof_path
                else:
                    answers[shorthand] = answer

    # Append data to the existing JSON file
    append_to_json(answers)

def handle_proof(proof):
    if proof.startswith('http'):
        # If it's a link, download the image
        download_path = os.path.join(MEDIA_DIR, f"{date.today().strftime('%Y-%m-%d')}.jpg")
        download_image(proof, download_path)
        return download_path
    else:
        # If it's a local filepath, copy the image
        copy_path = os.path.join(MEDIA_DIR, f"{date.today().strftime('%Y-%m-%d')}.jpg")
        copyfile(proof, copy_path)
        return copy_path

def download_image(url, destination):
    response = requests.get(url, stream=True)
    with open(destination, 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)

def append_to_json(data):
    # If the file doesn't exist, create it with the current data
    if not os.path.isfile(storage_file_name):
        with open(storage_file_name, 'w') as file:
            json.dump([data], file, indent=2)
    else:
        # If the file exists, load the existing data, append the new data, and save
        with open(storage_file_name, 'r') as file:
            existing_data = json.load(file)
        existing_data.append(data)
        with open(storage_file_name, 'w') as file:
            json.dump(existing_data, file, indent=2)

if __name__ == '__main__':
    # Create 'media' directory if it doesn't exist
    os.makedirs(MEDIA_DIR, exist_ok=True)

    collect_data()

import requests
import sys
import os

def upload_file(filepath, job_id, callback_url):
    with open(filepath, 'rb') as f:
        files = {'file': (f'{job_id}.docx', f)}
        data = {
            'job_id': job_id,
            'api_key': os.getenv('CALLBACK_KEY')
        }
        response = requests.post(callback_url, files=files, data=data)
        response.raise_for_status()

if __name__ == "__main__":
    upload_file(sys.argv[1], sys.argv[2], sys.argv[3])

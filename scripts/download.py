import sys
import requests

def download_pdf(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

if __name__ == "__main__":
    download_pdf(sys.argv[1], sys.argv[2])

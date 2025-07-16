import requests
import sys

def download_file(url, filename):
    headers = {'User-Agent': 'PDFConverter/1.0'}
    with requests.get(url, headers=headers, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

if __name__ == "__main__":
    download_file(sys.argv[1], sys.argv[2])

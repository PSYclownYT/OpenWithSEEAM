from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile


def download_and_unzip(url, name):
    extract_to = 'SeeamApps/{name}'
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)
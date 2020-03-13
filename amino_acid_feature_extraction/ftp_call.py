"""
Main module
Script to pull down the aaindex1 file from ftp://ftp.genome.jp/pub/db/community/aaindex/
"""
import shutil
import urllib.request as request
from contextlib import closing
import time

class FtpGetFeatures:

    def __init__(self, base_url):
        self.base_url = base_url

        with closing(request.urlopen(self.base_url)) as r:
            with open('aaindex1', 'wb') as f:
                shutil.copyfileobj(r, f)

def main():
    FtpGetFeatures('ftp://ftp.genome.jp/pub/db/community/aaindex/aaindex1')
    time.sleep(10)

if __name__ == '__main__':
    main()

import argparse
import re
import subprocess

parser = argparse.ArgumentParser(description='Choosing your browser for you.')
parser.add_argument('url', type=str, nargs=1)
args = parser.parse_args()
url = args.url[0]

if re.match(r"https://.*\.github\.com.*", url):
    subprocess.Popen(['firefox', '-P', 'coding', url])
else:
    subprocess.Popen(['firefox', url])

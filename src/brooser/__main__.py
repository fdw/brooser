import argparse
import os
import re
import subprocess
from pathlib import Path

import tomli

parser = argparse.ArgumentParser(description='Choosing your browser for you.')
parser.add_argument('url', type=str, nargs=1)
args = parser.parse_args()
url = args.url[0]

config_path = Path(os.environ.get("XDG_CONFIG_HOME", "~/.config")).expanduser() / "brooser.conf"
with open(config_path, "rb") as f:
    configuration = tomli.load(f)

for key in configuration.keys():
    if key == "default":
        break

    for pattern in configuration[key]["urls"]:
        if re.match(pattern, url):
            subprocess.Popen(configuration[key]["command"].replace("%url", url).split(" "))
            exit(0)

subprocess.Popen(configuration["default"]["command"].replace("%url", url).split(" "))

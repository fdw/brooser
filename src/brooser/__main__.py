import argparse
import os
import re
import subprocess
from pathlib import Path
from typing import Dict, List

import tomli


def __get_url() -> str:
    parser = argparse.ArgumentParser(description="Choosing your browser for you.")
    parser.add_argument("url", type=str, nargs=1)
    args = parser.parse_args()
    return args.url[0]


def __read_config() -> Dict[str, Dict[str, str | List[str]]]:
    config_path = Path(os.environ.get("XDG_CONFIG_HOME", "~/.config")).expanduser() / "brooser.conf"
    with open(config_path, "rb") as f:
        return tomli.load(f)


def main():
    url = __get_url()
    configuration = __read_config()

    for key in configuration.keys():
        if key == "default":
            break

        for pattern in configuration[key]["urls"]:
            if re.match(pattern, url):
                subprocess.Popen(configuration[key]["command"].replace("%url", url).split(" "))
                exit(0)

    subprocess.Popen(configuration["default"]["command"].replace("%url", url).split(" "))


if __name__ == "__main__":
    main()

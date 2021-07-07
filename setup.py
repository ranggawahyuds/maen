#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#bancetzLau_
import os, sys

try:
    print("\n  \033[92m[!!] Checking availability of pip..\033[0m")
    import pip
    print("\n  \033[92m[!!] OK..\033[0m")
except:
    os.system("sudo apt update -y && sudo apt upgrade -y && sudo apt install python3-pip -y")
    print("\n  \033[92m[!!] OK..\033[0m")

url = "https://github.com/bancetzLaut/BL378-sp/releases/download/1.0.0b0"

if 'com.termux' in os.path.expanduser('~').split('/'):
    cmd = f"{url}/BL378sp-1.0.0b0-cp39-cp39-linux_aarch64.whl"
else:
    cmd = f"{url}/BL378sp-1.0.0b0-cp38-cp38-linux_x86_64.whl"


print("\n  \033[92m[!!] Installing additional module..\033[0m")
os.system(f"{sys.executable} -m pip install -U --timeout 37 --no-cache-dir {cmd}")

print("\n  \033[92m[!!] Downloading Config..\033[0m")
os.system(f"curl -# -o BLConfig.py -L {url}/cfg.py")

print("\n  \033[92m[!!] Downloading Main file..\033[0m")
os.system(f"curl -# -o jakesp.py -L {url}/main.py")

print("\n  \033[92m[!!] Cleaning setup area..\033[0m")
os.system(f"rm setup.py")

print("\n  \033[92m[!!] OK..\033[0m")

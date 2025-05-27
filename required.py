import os
import subprocess

modules = [
    "requests", "Topython", "pysocks", "curl2pyreqs", "pycountry", "pyfiglet",
    "pystyle", "fade", "colorama", "fake_useragent", "ms4", "uuid"
]

for mod in modules:
    try:
        __import__(mod)
    except ImportError:
        print(f"Installing {mod}...")
        subprocess.run(["pip", "install", mod], check=True)

print("✅ All required modules are installed!")

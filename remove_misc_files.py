import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("directory_name")
args = parser.parse_args()
for root, dirs, files in os.walk("."):
    for file in files:
        if not file.startswith("0 ") and not file.endswith(".description") and not file.endswith(".txt"):
            # Remove the file
            filepath = os.path.join(root, file)
            os.remove(filepath)
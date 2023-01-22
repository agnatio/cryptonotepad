import os
# print(os.environ)
import re


print(os.getcwd())

data = []

with open(f"{os.getcwd()}/.env") as f:
    for line in f:
        print(line)
        match = re.search(r"=(.*)", line)
        print(match.group(1))

   
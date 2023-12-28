import os
import sys
import yaml
import json

resume_file = "Resume.yml"

def parseYAML():
    with open(resume_file, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
    
def convertToJSON():
    with open("Resume"+".json", "w", encoding="utf-8") as jsonOut:
        json.dump(parseYAML(), jsonOut, indent=4, ensure_ascii=False)

convertToJSON()

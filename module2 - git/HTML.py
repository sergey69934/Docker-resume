import json
from json2html import *

with open('Resume.json') as f:
    d = json.load(f)
    scanOutput = json2html.convert(json=d)
    htmlReportFile = "Resume.html"
    with open(htmlReportFile,"w") as htmlfile:
        htmlfile.write(str("""<!DOCTYPE html><HTML lang='ru'><HEAD><TITLE>Resume</TITLE><link href="styles.css" rel="stylesheet" /></HEAD><H1 ALIGN=CENTER>  Resume </H1>"""))
        htmlfile.write(str(scanOutput))
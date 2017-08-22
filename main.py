#!/usr/bin/python2.7
import sys
from app.microsoft.emotion import analyze
from app.instagram.get import get_pictures

# First argument - Microsoft Azure Emotion API Key
# Second argument - Emotion API Endpoint region (e.g. "westus")
# Third arguement - Instagram Username
urls = get_pictures(sys.argv[3])

for url in urls:
  print url
  analyze(sys.argv[1], sys.argv[2], url)

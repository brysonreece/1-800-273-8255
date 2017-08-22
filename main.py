#!/usr/bin/python2.7
import sys
from app.microsoft.emotion import analyze

# First argument - Microsoft Azure Emotion API Key
# Second argument - Emotion API Endpoint region (e.g. "westus")
# Third arguement - URL of photo
analyze(sys.argv[1], sys.argv[2], sys.argv[3])

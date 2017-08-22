import Tkinter as tk
from ScrolledText import *
import urllib, json, operator
from PIL import ImageTk, Image

MAX_WINDOW_HEIGHT = 500

def render(url, data):
  window = tk.Tk()
  window.title("Preview")
  window.configure(background="grey")

  file = open('preview', 'wb')
  file.write(urllib.urlopen(url).read())
  file.close()

  image = Image.open("preview")
  imageWidth, imageHeight = image.size

  scaledHeight = imageHeight * (float(MAX_WINDOW_HEIGHT) / imageHeight)
  scaledWidth = imageWidth * (float(MAX_WINDOW_HEIGHT) / imageHeight)
  scaledSize = (int(scaledWidth), int(scaledHeight))

  image = image.resize(scaledSize)
  photo = ImageTk.PhotoImage(image)

  canvas = tk.Canvas(window)
  canvas.pack(side="left", fill="both", expand="true")

  canvas_image = canvas.create_image(0, 0, anchor="nw", image = photo)
  
  # left, top, left + width, top + height
  for result in json.loads(data):
    x0 = result["faceRectangle"]["left"] * (float(MAX_WINDOW_HEIGHT) / imageHeight)
    y0 = result["faceRectangle"]["top"] * (float(MAX_WINDOW_HEIGHT) / imageHeight)
    x1 = x0 + result["faceRectangle"]["width"] * (float(MAX_WINDOW_HEIGHT) / imageHeight)
    y1 = y0 + result["faceRectangle"]["height"] * (float(MAX_WINDOW_HEIGHT) / imageHeight)
    
    emotions = {
      "anger": float(result["scores"]["anger"]),
      "contempt": float(result["scores"]["contempt"]),
      "disgust": float(result["scores"]["disgust"]),
      "fear": float(result["scores"]["fear"]),
      "happiness": float(result["scores"]["happiness"]),
      "neutral": float(result["scores"]["neutral"]),
      "sadness": float(result["scores"]["sadness"]),
      "surprise": float(result["scores"]["surprise"])
    }

    suspectedEmotion = max(emotions.iteritems(), key=operator.itemgetter(1))[0]

    box = canvas.create_rectangle(x0, y0, x1, y1, width=5, outline="red")
    text = canvas.create_text(((x0 - x1) / 2) + x1, y1 + 15, text=suspectedEmotion, fill="red")

  #infoPanel = ScrolledText(window, undo=True)
  #infoPanel['font'] = ('consolas', '12')
  #infoPanel.pack(expand="true", fill='both')
  #infoPanel.insert('insert', data) 
  
  window.geometry(str(int(scaledWidth)) + "x" + str(int(scaledHeight)))
  window.mainloop() 
  file.close()

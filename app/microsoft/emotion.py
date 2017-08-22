import httplib, json, urllib
import app.gui.preview as preview
import app.instagram.get as instagram

def analyze(key, region, url):
    headers = {
        # Request headers. Replace the placeholder key below with your subscription key.
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key,
    }

    params = urllib.urlencode({
    })

    # Replace the example URL below with the URL of the image you want to analyze.
    body = "{ 'url': '" + url + "' }"

    try:
        # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
        #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
        #   URL below with "westcentralus".
        conn = httplib.HTTPSConnection(region + '.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        if (data != "[]"):
          json_data = json.loads(data)
          pretty_json = json.dumps(json_data, indent=4, sort_keys=True)
	  preview.render(url, pretty_json)
        conn.close()
    except Exception as e:
        print("[Error] {0}".format(e.message))

    return

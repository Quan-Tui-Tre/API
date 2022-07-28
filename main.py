import requests
import base64
import json
def solve_captcha(base64_encode):
    try:
        json_data =  {
                "requests": [{
                    "image": {
                        "content": str(base64_encode)
                    },
                    "features": [{"type": "TEXT_DETECTION"}]
                }]
            }
        req = requests.post(
        url = 'https://content-vision.googleapis.com/v1/images:annotate',
        headers = {
            'x-origin': 'https://explorer.apis.google.com',
        },
        params = {
            'alt': 'json',
            'key': 'AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM',
        },
        json = json_data
    )
        captcha_answer = req.json()['responses'][0]["textAnnotations"][0]["description"]
        return json.dumps({'status': 'success', 'text': captcha_answer})
    except:
        return req.json()

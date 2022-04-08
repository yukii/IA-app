import requests, uuid, json

def translate_text(text, langue_origin, langue_tar):
    # Add your subscription key and endpoint
    subscription_key = "7bdcdaca87474cb2bd46e3442e39ee46"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "francecentral"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': langue_origin,
        'to': langue_tar
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]


    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    json_res = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
    return response[0]["translations"][0]["text"]

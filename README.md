
# Google Gemini API Proxy Server

Aktuell ist die API von Google Gemini noch nicht in Deutschland verfügbar. 
Um die API jetzt schon in Deutschland verfügbar zu machen, kann man über z.B. Linode oder Hetzner einen Server mit dem Standord USA günstig mieten, dieses Flask Skript darauf installieren und somit die Google Gemini API auch in Deutschland nutzen, da der Abruf dann wie ein Proxy funktioniert.


## Gemini API Proxy Server verwenden

Projekt runterladen

```bash
  git clone https://github.com/speetzial/GeminiAPIProxy
```

Gehe in den Projektordner

```bash
  cd GeminiAPIProxy
```

Erforderliche Pakete installieren

```bash
  #Linux
  pip3 install -r requirements.txt

  #Windows
  pip install -r requirements.txt
```

.env Datei anlegen

```bash
GEMINI_API_KEY= <DEIN GOOGLE GEMINI API KEY>
SERVER_API_KEY= <DEIN WUNSCH API KEY FÜR DEN PROXY>
```

Server starten

```bash
#Linux
python3 app.py

#Windows
python app.py
```
## Environment Variables

`GEMINI_API_KEY`

`SERVER_API_KEY`


## Usage/Examples


Python
```python
import requests

url = "http://YOURDOMAIN.DE:5000/text"

payload = 'promt=<ENTER PROMT HERE>'
headers = {
		'key': '<SERVER_API_KEY>',
		'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

Javascript (Fetch)
```javascript
var myHeaders = new Headers();
myHeaders.append("key", "<SERVER_API_KEY>");
myHeaders.append("Content-Type", "application/x-www-form-urlencoded");

var urlencoded = new URLSearchParams();
urlencoded.append("promt", "<ENTER PROMT HERE>");

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: urlencoded,
  redirect: 'follow'
};

fetch("http://YOURDOMAIN.DE:5000/text", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```


Javascript (jQuery)
```javascript
var settings = {
  "url": "http://YOURDOMAIN.DE:5000/text",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "key": "<SERVER_API_KEY>",
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "data": {
    "promt": "<ENTER PROMT HERE>"
  }
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

PHP
```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'http://YOURDOMAIN.DE:5000/text',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => 'promt=<ENTER PROMT HERE>',
  CURLOPT_HTTPHEADER => array(
    'key: <SERVER_API_KEY>',
    'Content-Type: application/x-www-form-urlencoded'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;

?>
```
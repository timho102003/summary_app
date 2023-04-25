# OpenAI Summarize App

## Goal: 
Developed and deployed RestAPI with `beam.cloud`

## Depedency:
- openai
- beam

## Connect to remote beam server:
```bash
beam start app.py
```

## Local Test:
```bash
beam % serve
```

## Deploy:
```bash
beam % exit # Leave the remote container
beam deploy app.py
```

## BEAM:
[beam website](https://docs.beam.cloud/introduction)

## Query:

### Command:
``` bash
curl -X POST --compressed <endpoint-url> \
   -H 'Accept: */*' \
   -H 'Accept-Encoding: gzip, deflate' \
   -H 'Authorization: Basic <auth_key>' \
   -H 'Connection: keep-alive' \
   -H 'Content-Type: application/json' \
   -d '{"api_key": <openai-apikey>, "article": "xxxxxxxxxx, summarize for me"}'
```
### Response:
```{"response": <summary string>}```
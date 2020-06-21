# uncurl to Python

## Record network

1. Press CTRL + Shift + I and go to *Network*
2. Look for ```jsonrpc``` package
3. Right click and ```Copy > Copy as cURL```

### Run curl command

Paste copied curl command into the terminal and check the output.

```bash
curl 'https://www2.deepl.com/jsonrpc' \
  -H 'authority: www2.deepl.com' \
  -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36' \
  -H 'content-type: text/plain' \
  -H 'accept: */*' \
  -H 'origin: https://www.deepl.com' \
  -H 'sec-fetch-site: same-site' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.deepl.com/translator' \
  -H 'accept-language: en-US;q=0.8,en;q=0.7' \
  --data-binary '{"jsonrpc":"2.0","method" : "LMT_handle_jobs","params":{"jobs":[{"kind":"default","raw_en_sentence":"This is text","raw_en_context_before":[],"raw_en_context_after":[],"preferred_num_beams":4}],"lang":{"user_preferred_langs":["FR","EN","DE"],"source_lang_user_selected":"auto","target_lang":"EN"},"priority":1,"commonJobParams":{},"timestamp":1592743944801},"id":3490003}' \
  --compressed
```

```json
{
  "jsonrpc":"2.0",
  "id":3490003,
  "result":{
    "translations":[
      {
        "beams":[
          {
            "postprocessed_sentence":"This is text",
            "num_symbols":4,
            "score":1.0,
            "totalLogProb":0.0
          }
        ],
        "quality":"normal"
      }
    ],
    "target_lang":"EN",
    "source_lang":"EN",
    "source_lang_is_confident":false,
    "timestamp":1592744780,
    "date":"20200621"
  }
}
```

You can probably delete the cookies.

```bash
xclip -selection clipboard -o > curl.sh
```

### Escape command

```bash
cat curl.sh | tr '\\\r\n' ' ' | tr -s " " | sed 's/"/\\"/g' > escaped.sh
```

### Uncurl to file

```bash
cat escaped.sh | uncurl > curl.py
```

## All in one

```bash
xclip -selection clipboard -o | tr '\\\r\n' ' ' | tr -s " " | sed 's/"/\"/g' | uncurl > curl.py
```

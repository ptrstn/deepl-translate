import json
import time

import requests

API_URL = "https://www2.deepl.com/jsonrpc"
SUPPORTED_LANGUAGES = ["DE", "EN", "FR", "ES", "PT", "IT", "NL", "PL", "RU", "JA", "ZH"]


def generate_request_headers():
    return {
        "Host": "www2.deepl.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-type": "text/plain",
        "Content-Length": "366",  # TODO calculate content length
        "Origin": "https://www.deepl.com",
        "Connection": "keep-alive",
        "Referer": "https://www.deepl.com/translator",
    }


def generate_request_data(text, source_language, target_language):
    data_json = {
        "jsonrpc": "2.0",
        "method": "LMT_handle_jobs",
        "params": {
            "jobs": [
                {
                    "kind": "default",
                    "raw_en_sentence": text,
                    "raw_en_context_before": [],
                    "raw_en_context_after": [],
                    "preferred_num_beams": 4,
                }
            ],
            "lang": {
                "user_preferred_langs": [source_language, target_language],
                "source_lang_computed": source_language,
                "target_lang": target_language,
            },
            "priority": 1,
            "commonJobParams": {},
            "timestamp": int(time.time() * 1000),
        },
        "id": 64340017,  # TODO find way to generate id
    }

    return json.dumps(data_json)


def extract_translation(json_response):
    return json_response["result"]["translations"][0]["beams"][0][
        "postprocessed_sentence"
    ]


def get_language_abbreviation(language):
    return {
        "de": "DE",
        "en": "EN",
        "fr": "FR",
        "es": "ES",
        "pt": "PT",
        "it": "IT",
        "nl": "NL",
        "pl": "PL",
        "ru": "RU",
        "ja": "JA",
        "zh": "ZH",
        "german": "DE",
        "english": "EN",
        "french": "FR",
        "spanish": "ES",
        "portuguese": "PT",
        "italian": "IT",
        "dutch": "NL",
        "polish": "PL",
        "russian": "RU",
        "japanese": "JA",
        "chinese": "ZH",
    }.get(language.lower())


def translate(source_language="DE", target_language="RU", text="Guten Tag"):
    language_from = get_language_abbreviation(source_language)
    language_to = get_language_abbreviation(target_language)

    assert (
        language_from in SUPPORTED_LANGUAGES
    ), f"Unsupported language: {source_language} -> {target_language}"
    assert (
        language_to in SUPPORTED_LANGUAGES
    ), f"Unsupported language: {source_language} -> {target_language}"

    data = generate_request_data(
        text=text, source_language=language_from, target_language=language_to
    )

    headers = generate_request_headers()

    response = requests.post(API_URL, data=data, headers=headers,)
    return extract_translation(response.json())

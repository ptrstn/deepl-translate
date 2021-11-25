import json

import requests

from deepl.extractors import extract_split_sentences, extract_translated_sentences
from deepl.generators import (
    generate_split_sentences_request_data,
    generate_translation_request_data,
)
from deepl.settings import API_URL
from deepl.utils import abbreviate_language

headers = {
    "accept": "*/*",
    "accept-language": "en-US;q=0.8,en;q=0.7",
    "authority": "www2.deepl.com",
    "content-type": "application/json",
    "origin": "https://www.deepl.com",
    "referer": "https://www.deepl.com/translator",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": (
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/83.0.4103.97 Mobile Safari/537.36"
    ),
}


def split_into_sentences(text, **kwargs):
    data = generate_split_sentences_request_data(text, **kwargs)
    response = requests.post(API_URL, data=json.dumps(data), headers=headers)
    response.raise_for_status()

    json_response = response.json()
    sentences = extract_split_sentences(json_response)

    return sentences


def request_translation(source_language, target_language, text, **kwargs):
    sentences = split_into_sentences(text, **kwargs)
    data = generate_translation_request_data(
        source_language, target_language, sentences, **kwargs
    )
    response = requests.post(API_URL, data=json.dumps(data), headers=headers)
    return response


def translate(source_language, target_language, text, **kwargs):
    source_language = abbreviate_language(source_language)
    target_language = abbreviate_language(target_language)

    response = request_translation(source_language, target_language, text, **kwargs)
    response.raise_for_status()

    json_response = response.json()
    translated_sentences = extract_translated_sentences(json_response)
    translated_text = " ".join(translated_sentences)

    return translated_text

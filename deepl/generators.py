from deepl.hacks import generate_timestamp
from deepl.settings import MAGIC_NUMBER, SUPPORTED_FORMALITY_TONES


def generate_split_sentences_request_data(text, identifier=MAGIC_NUMBER, **kwargs):
    return {
        "jsonrpc": "2.0",
        "method": "LMT_split_into_sentences",
        "params": {
            "texts": [text],
            "lang": {"lang_user_selected": "auto", "user_preferred_langs": []},
        },
        "id": identifier,
    }


def generate_jobs(sentences, beams=1):
    jobs = []
    for idx, sentence in enumerate(sentences):
        job = {
            "kind": "default",
            "raw_en_sentence": sentence,
            "raw_en_context_before": sentences[:idx],
            "raw_en_context_after": [sentences[idx + 1]]
            if idx + 1 < len(sentences)
            else [],
            "preferred_num_beams": beams,
        }
        jobs.append(job)
    return jobs


def generate_common_job_params(formality_tone):
    if not formality_tone:
        return {}
    if formality_tone not in SUPPORTED_FORMALITY_TONES:
        raise ValueError(f"Formality tone '{formality_tone}' not supported.")
    return {"formality": formality_tone}


def generate_translation_request_data(
    source_language,
    target_language,
    sentences,
    identifier=MAGIC_NUMBER,
    alternatives=1,
    formality_tone=None,
):
    return {
        "jsonrpc": "2.0",
        "method": "LMT_handle_jobs",
        "params": {
            "jobs": generate_jobs(sentences, beams=alternatives),
            "lang": {
                "user_preferred_langs": [target_language, source_language],
                "source_lang_computed": source_language,
                "target_lang": target_language,
            },
            "priority": 1,
            "commonJobParams": generate_common_job_params(formality_tone),
            "timestamp": generate_timestamp(sentences),
        },
        "id": identifier,
    }

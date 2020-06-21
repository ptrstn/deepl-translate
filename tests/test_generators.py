from deepl.generators import generate_jobs


def test_generate_jobs_with_one_sentences():
    sentences = ["Forever alone."]
    expected_jobs = [
        {
            "kind": "default",
            "raw_en_sentence": "Forever alone.",
            "raw_en_context_before": [],
            "raw_en_context_after": [],
            "preferred_num_beams": 3,
        }
    ]

    assert generate_jobs(sentences, beams=3) == expected_jobs


def test_generate_jobs_with_three_sentences():
    sentences = ["First.", "Second.", "Third."]
    expected_jobs = [
        {
            "kind": "default",
            "raw_en_sentence": "First.",
            "raw_en_context_before": [],
            "raw_en_context_after": ["Second."],
            "preferred_num_beams": 1,
        },
        {
            "kind": "default",
            "raw_en_sentence": "Second.",
            "raw_en_context_before": ["First."],
            "raw_en_context_after": ["Third."],
            "preferred_num_beams": 1,
        },
        {
            "kind": "default",
            "raw_en_sentence": "Third.",
            "raw_en_context_before": ["First.", "Second."],
            "raw_en_context_after": [],
            "preferred_num_beams": 1,
        },
    ]

    assert generate_jobs(sentences) == expected_jobs

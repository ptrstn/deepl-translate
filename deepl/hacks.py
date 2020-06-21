import time
from random import randrange


def calculate_valid_timestamp(timestamp, i_count):
    try:
        return timestamp + (i_count - timestamp % i_count)
    except ZeroDivisionError:
        return timestamp


def generate_timestamp(sentences):
    now = int(time.time() * 1000)
    i_count = 1
    for sentence in sentences:
        i_count += sentence.count("i")

    return calculate_valid_timestamp(now, i_count)


def generate_id():
    return randrange(1_000_000, 100_000_000)

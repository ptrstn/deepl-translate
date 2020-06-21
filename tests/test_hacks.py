from deepl.hacks import calculate_valid_timestamp, generate_id


def test_calculate_valid_timestamp():
    assert 10 == calculate_valid_timestamp(timestamp=10, i_count=0)
    assert 11 == calculate_valid_timestamp(timestamp=10, i_count=1)
    assert 12 == calculate_valid_timestamp(timestamp=10, i_count=2)
    assert 12 == calculate_valid_timestamp(timestamp=10, i_count=3)
    assert 12 == calculate_valid_timestamp(timestamp=10, i_count=4)
    assert 15 == calculate_valid_timestamp(timestamp=10, i_count=5)
    assert 12 == calculate_valid_timestamp(timestamp=10, i_count=6)


def test_generate_id():
    assert 100_000_000 > generate_id() > 1_000_000

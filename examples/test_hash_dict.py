from hash_dict import hash_dict

def test_hash_dict():
    example_dict = {'hi':'there'}
    new_dict = {hash_dict(example_dict) : 0}
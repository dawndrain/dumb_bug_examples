from partition import partition

def test_partition():
    example_list = [1,2,3,4,5,6,7]
    partitioned_list = partition(example_list,3)
    assert len(partitioned_list) == 3
    lengths = [3,2,2]
    for length,sub_list in zip(lengths,partitioned_list):
        assert len(sub_list) == length
    
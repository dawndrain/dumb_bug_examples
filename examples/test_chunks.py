from chunks import chunks

def test_chunks():
    example_list = [1,2,3,4,5,6,7]
    example_chunks = [[1,2,3],[4,5,6],[7]]
    for gold_chunk,gen_chunk in zip(example_chunks,chunks(example_list,3)):
        assert gen_chunk == gold_chunk

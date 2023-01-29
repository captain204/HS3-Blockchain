from backend.util.hash_function import  hash_function

def test_hash():
    #It should create the same hash with arguments of different data types in any other
    assert hash_function(1,[2],'three') == hash_function('three',1,[2])
    assert hash_function('foo') == 'b2213295d564916f89a6a42455567c87c3f480fcd7a1c15e220f17d7169a790b'



    
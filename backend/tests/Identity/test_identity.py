from backend.identity.identity import Identity
from backend.blockchain.blockchain import Blockchain


def test_verify_valid_signature():
    data = { 'New': 'test_data' }
    identity = Identity()
    signature = identity.sign(data)

    assert Identity.verify(identity.public_key, data, signature)

def test_verify_invalid_signature():
    data = { 'foo': 'test_data' }
    identity = Identity()
    signature = identity.sign(data)

    assert not Identity.verify(Identity().public_key, data, signature)

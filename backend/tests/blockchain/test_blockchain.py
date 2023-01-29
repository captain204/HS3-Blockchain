from ast import boolop
import pytest
from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA


def test_blockchain_instance():
    blockchain = Blockchain()

    #test to ensure first block is the genesis block
    assert blockchain.chain[0].hash == GENESIS_DATA['hash']


def test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data


@pytest.fixture
def create_three_blocks():
    blockchain = Blockchain()
    for i in range(3):
        blockchain.add_block(i)
    return blockchain

def test_is_valid_chain(create_three_blocks):
    Blockchain.is_valid_chain(create_three_blocks.chain)


def test_is_valid_chain_bad_genesis(create_three_blocks):
    create_three_blocks.chain[0].hash = 'wrong hash'

    with pytest.raises(Exception, match='The genesis block must be valid'):
        Blockchain.is_valid_chain(create_three_blocks.chain)

def test_replace_chain(create_three_blocks):
    blockchain = Blockchain()
    blockchain.replace_chain(create_three_blocks.chain)
    assert blockchain.chain == create_three_blocks.chain

def test_replace_chain_not_longer(create_three_blocks):
    blockchain = Blockchain()

    with pytest.raises(Exception, match='Cannot be replaced. Incoming chain must be longer'):
        create_three_blocks.replace_chain(blockchain.chain)

def test_replace_chain_with_bad_chain(create_three_blocks):
    blockchain = Blockchain()
    create_three_blocks.chain[1].hash = 'wrong hash'

    with pytest.raises(Exception, match='Cannot be replaced. The incoming chain is invalid'):
        blockchain.replace_chain(create_three_blocks.chain)



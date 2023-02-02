from backend.blockchain.block import Block
from backend.identity.transaction import Transaction


class Blockchain:
    """
        Blockchain is a public ledger of transactions
        Implemented as a list of blocks -data sets of transactions
    """
    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1],data))
    
    def __repr__(self) -> str:
        return f'Blockchain:{self.chain}'

    def replace_chain(self,chain):
        """
            Replace the local chain with the incoming chain based on the following rules
            -The incoming chain is longer than the local chain
            -The incoming chain is formatted properly
        """
        if len(chain) <= len(self.chain):
            raise Exception('Cannot be replaced. Incoming chain must be longer')

        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Cannot be replaced. The incoming chain is invalid {e}')
        self.chain = chain


    def to_json(self):
        """
            Serialize Blockchain
        """
      
        return list(map(lambda block:block.to_json(), self.chain))
        
    
    @staticmethod
    def is_valid_chain(chain):
        """
            Valid incoming chain
            Enforce the following rules of the blockchain
            -The chain must start with the genesis block
            -Blocks must be formatted correctly
        """

        if chain[0] != Block.genesis():
            raise Exception('The genesis block must be valid')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block,block)

    


def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block([{'facility':'Rayfield Medical','diagnosis':'Maleria'},{'facility':'Rayfield Medical','diagnosis':'Maleria'}])
    blockchain.add_block(['patient one',12039])

    print(blockchain)
    print(f'blockchain.py __name__:{__name__}')


if __name__ =='__main__':
    main()
import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from decouple import config

from backend.blockchain.block import Block
from backend.blockchain.blockchain import Blockchain

pnconfig = PNConfiguration()

pnconfig.subscribe_key = config('SUBSCRIBE')
pnconfig.publish_key = config('PUBLISH')




CHANNELS ={
    'TEST':'TEST',
    'BLOCK':'BLOCK'
}


class Listener(SubscribeCallback):
    def __init__(self, blockchain):
        self.blockchain = blockchain
        

    def message(self, pubnub, message_object):
        print(f'\n Incoming message_object{message_object.channel} |Message{message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']:
            block  = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                print('\n Successfully replaced the local chain')
            except Exception as e:
                print(f'\n --Did not replace chain {e}')



class Pubsub():
    """
        Handles the public susbscribe layer of the application
        Provides communication between the nodes of the blockchain network
    """
    def __init__(self,blockchain):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([CHANNELS.values()]).execute()
        self.pubnub.add_listener(Listener(blockchain))

    def publish(self, channel, message):
        """
            Publish the message object to the channel
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self,block):
        """
            Broadcast a block object to all nodes
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())

def main():
    blockchain = Blockchain()

    pubsub = Pubsub(blockchain)
    
    time.sleep(1)

    pubsub.publish(CHANNELS['TEST'], {'New':'Block'})
    

if __name__  == '__main__':
    main()


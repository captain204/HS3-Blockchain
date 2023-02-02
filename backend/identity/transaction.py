import time
import uuid

from backend.identity.identity import Identity


class Transaction:
    """
    Document of writing a transaction to the blockchain
    """
    def __init__(
        self,
        sender_identity=None,
        data=None,
        id=None,
        input=None
    ):
        self.id = id or str(uuid.uuid4())[0:8]
        self.data = data or self.create_output(
            sender_identity,
            data,
        )
        self.input = input or self.create_input(sender_identity, self.data)


    def create_input(self, sender_identity,data):
        """
        Structure the input data for the transaction.
        Sign the transaction and include the sender's public key and address
        """
        return {
            'timestamp': time.time_ns(),
            'address': sender_identity.address,
            'public_key': sender_identity.public_key,
            'signature': sender_identity.sign(data)
        }

    def to_json(self):
        """
        Serialize the transaction.
        """
        return self.__dict__

    @staticmethod
    def from_json(transaction_json):
        """
        Deserialize a transaction's json representation back into a
        Transaction instance
        """
        return Transaction(**transaction_json)

   

def main():

    transaction_data = { 'Hosptal': 'New crescent',
            'Patient':'John Emmanuel',
            'Physician':'Dr Oluwafemi',
            'Diagnosis':'Malaria',
            'Description':'Patients is struggling from sever malaria',
            'Medication':'Arthemeter'
     }

    transaction = Transaction(Identity(), transaction_data)
    print(f'transaction.__dict__: {transaction.__dict__}')

    transaction_json = transaction.to_json()
    restored_transaction = Transaction.from_json(transaction_json)
    print(f'restored_transaction.__dict__: {restored_transaction.__dict__}')

if __name__ == '__main__':
    main()
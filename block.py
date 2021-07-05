# Classic hashlib library, used for hashing. We'll use SHA256 particularly
import hashlib

class Block:
    def __init__(self, data: str, previous_hash: _hashlib.HASH):
        """Initializes the block with the given data and previous hash

        Args:
            data (str): Information to be stored in blockchain
            previous_hash (_hashlib.HASH): Hash  object of the previous block
        """
        self.data = data
        self.previous_hash = previous_hash
        # Hash of the current block
        self.hash = hashlib.sha256()
        # This is nonce (number used once), used for achieving hash which satisfies difficulty level.
        self.nonce = 0
    
    def __str__(self):
        # String representation of the block, we will use this string and hash it
        return f"{self.previous_hash.hexdigest()}{self.data}{self.nonce}"
    
    def mine(self, difficulty: int):
        """Mines the block with given difficulty level

        Args:
            difficulty (int): How many number of leading zeros should be there in hashes
        """
        # Encoding string and finding initial hash
        self.hash.update(str(self).encode('utf-8'))

        # We will repetedly find hash untill our difficulty level satisfies
        while int(self.hash.hexdigest(), 16) > 2 ** (256 - difficulty):
            # If not the desired hash, then increment the nonce 
            self.nonce += 1
            # Reinitializing the hash and finding new hash with the new nonce
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf-8'))
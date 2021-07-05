import hashlib
from block import Block

class Chain:
    def __init__(self, difficulty: int):
        """Initializes the chain with the difficulty level

        Args:
            difficulty (int): It shows how many number of leading zeros you want in hash of a block. More difficulty level will make mining of a block harder.
        """
        # Sets the difficulty level
        self.difficulty: int = difficulty
        # List of blocks that are already mined
        self.blocks: list[Block] = []
        # List of data that are yet to be mined
        self.pool: list[str] = []
        # Creating origin block
        self.create_origin_block()
    
    def proof_of_work(self, block: Block) -> bool:
        """Verifies the work

        Args:
            block (Block): block to be mined

        Returns:
            bool: True if block is successfully mined, False otherwise
        """
        # Creating new hash object and finding hash of the given block
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        # If the calculated hash and the hash of the block is same and hash satisfies the given difficulty level and it's previous hash is matching with the hash of the last block in the list of blocks that are already mined then only return True.
        return hash.hexdigest() == block.hash.hexdigest() and int(hash.hexdigest(), 16) < 2 ** (256 - self.difficulty) and block.previous_hash == self.blocks[-1].hash
    
    def add_to_chain(self, block: Block):
        """Adds the block to the chain if it satisfies the requirments

        Args:
            block (Block): block to be added to the chain
        """
        if self.proof_of_work():
            self.blocks.append(block)
        
    def add_to_pool(self, data: str):
        """Adds the data to the pool list

        Args:
            data (str): Data to be mined
        """
        self.pool.append(data)
    
    def create_origin_block(self):
        """Creates the origin block for the chain
        """
        # creating a new hash object and finding new hash with empty string.
        hash = hashlib.sha256()
        hash.update(''.encode('utf-8'))
        # Instantiating a new block with data 'Origin', and for previous hash we'll give the hash generated by empty string
        origin_block = Block('Origin', hash)
        # Mine the block with the difficulty level of the chain
        origin_block.mine(self.difficulty)
        # Appending it to the mined block list
        self.blocks.append(origin_block)

    def mine(self): 
        """Mines the block from pool list
        """
        # Checking if there is anything to be mined 
        if len(self.pool) > 0:
            # Getting data from the pools list and removing it from the list
            data = self.pool.pop()
            # Instantiating the block with the given data and hash of the last block in the blocks list
            block = Block(data, self.blocks[-1].hash)
            # mining the block on the given difficulty level
            block.mine(self.difficulty)
            # Adding the block to the chain
            self.add_to_chain(block)
            # Showing block details
            self.verbose(block)

    def verbose(self, block: Block):
        """Shows the block's details

        Args:
            block (Block): block
        """
        print('\n\n==============================')
        print('Hash:\t\t', block.hash.hexdigest())
        print('Previous Hash:\t', block.previous_hash.hexdigest())
        print('Nounce:\t\t', block.nonce)
        print('Data:\t\t', block.data)
        print('\n\n==============================')
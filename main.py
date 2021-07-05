from chain import Chain

# Initializing chain with the difficulty level of 20.
chain = Chain(20)

# Demo for mining of blocks
for i in range(5):
    # Adding to the pool
    chain.add_to_pool(str(i))
    # Mining the block
    chain.mine()
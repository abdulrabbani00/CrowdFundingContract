from brownie import MockV3Aggregator, network, config, accounts
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local']
DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    
def deploy_mocks():
    account = get_account()
    cur_network = network.show_active()
    
    print(f"The active network is: {cur_network}") 
    print("Deploying Mock") 
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, 
                                STARTING_PRICE, 
                                {"from": account}
        )
    print("Mocks Deployed")
    price_feed_address = MockV3Aggregator[-1].address
    
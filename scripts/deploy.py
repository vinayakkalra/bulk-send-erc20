from brownie import GoldCoin, network, config, BulkSender, accounts
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENV
from web3 import Web3
import csv


def deploy_erc20():
    account = get_account()
    token = GoldCoin.deploy(Web3.toWei(1000000000, "ether"), {"from": account})
    print(f"Contract Deployed to {token}")
    print(token.name())
    return token


def deploy_bulk_sender_contract():
    account = get_account()
    token = BulkSender.deploy({"from": account})
    print(f"BulkSender Contract Deployed to {token}")
    return token


def bulk_send(addresses, values):
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        erc20_address = deploy_erc20()
        bulk_sender_contract = deploy_bulk_sender_contract()
    else:
        # check the latest deployment
        if GoldCoin[-1] and BulkSender[-1]:
            erc20_address = GoldCoin[-1]
            bulk_sender_contract = BulkSender[-1]
        else:
            erc20_address = deploy_erc20()
            bulk_sender_contract = deploy_bulk_sender_contract()

    approve_tx = erc20_address.approve(
        bulk_sender_contract.address,
        sum(values),
        {"from": get_account()},
    )
    approve_tx.wait(1)
    print(f"approve tx {approve_tx}")
    tx = bulk_sender_contract.bulksendToken(
        erc20_address.address,
        addresses,
        values,
        {"from": get_account()},
    )
    tx.wait(1)
    print(f"token supply now {erc20_address.totalSupply()}")
    print(f"tokens with address 0 {erc20_address.balanceOf(get_account())}")


def read_csv():
    address = []
    values = []
    error = False
    with open("scripts/airdrop.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in spamreader:

            if Web3.isAddress(row[0]) and float(row[1]) > 0:
                address.append(row[0])
                values.append(Web3.toWei(row[1], "ether"))
            else:
                error = True
    if error:
        return ([], [])
    else:
        return (address, values)


def main():
    # bulk_send()
    (address, values) = read_csv()
    print("_______")
    print(address)
    print(values)
    print("_______")
    if len(address) == 0 or len(values) == 0 or len(address) != len(values):
        print("The address and values in the csv have spome problem")
    else:
        bulk_send(address, values)

# Batch send ERC20 tokens

Batch Send your ERC20 token to various multiple addresses. This is a great example if you are looking to airdrop your tokens to multiple people.

To execute a demo on rinkeby, please make note of the following:

1. Enter addresses that you wanna batch send along with value in the scripts/airdrop.csv file. 
2. The deploy.py script in scripts folder is used to create an erc20 token, deploy the bulksender contract as well as bulk send the addresses in airdrop.csv file.
3. If you want to refer to the contract, check BulkSender.sol in the contracts folder.
4. Run the below script to deploy things on the rinkeby chain:

```
brownie run scripts/deploy.py --network rinkeby
```


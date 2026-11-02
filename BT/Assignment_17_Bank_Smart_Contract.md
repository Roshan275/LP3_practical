# Assignment 17 — Bank account smart contract

## Aim

Write and deploy a Solidity contract on an Ethereum test network that lets each user deposit ETH, withdraw only their own available balance, and view their balance.

## What you need

- Browser access to [Remix IDE](https://remix.ethereum.org/).
- MetaMask connected to **Sepolia** and a small amount of Sepolia test ETH for deployment and transactions.
- No real ETH. Testnet ETH has no real-world value.

## Solidity program

Use the provided [Bank.sol](Bank.sol) file. It is the code supplied for this practical. It has an owner-only `Deposit`, `Withdraw`, and `showBalance`.

**Important behavior of this exact code:** `Withdraw()` is payable and decreases the internal `Balance` by `msg.value`, but it does not transfer ETH from the contract to the owner. It also needs a positive transaction value to be called. Therefore, it demonstrates a balance update but is not a real ETH withdrawal implementation. Do not send real funds to it. If your instructor expects an actual transfer, ask whether they want the contract corrected before deployment.

## Procedure in Remix

1. Open Remix IDE and create `Bank.sol`.
2. Copy the contents of the accompanying `Bank.sol` file into Remix and save it.
3. Open **Solidity Compiler**, select a compiler version `0.8.20` or compatible `0.8.x`, and compile `BankAccount.sol`.
4. Open **Deploy & Run Transactions**. In the environment selector, choose the injected MetaMask provider (the label can vary by Remix version).
5. In MetaMask, confirm the selected network is Sepolia and approve the connection request. Check the account shown in Remix.
6. Select `Bank` and click **Deploy**. Review the wallet confirmation and approve the testnet deployment.
7. After deployment confirms, expand the deployed contract in Remix. Record the contract address and deployment transaction hash.
8. To deposit, enter a small amount in Remix's **Value** field and choose the `ether` unit. Click `Deposit` and approve the transaction. Use Sepolia test ETH only.
9. Call `showBalance` from the deploying owner account and record the returned balance in wei. A different account should fail the owner check.
10. To demonstrate the code's `Withdraw`, enter a small positive amount in the **Value** field, then click `Withdraw` and confirm. The call decreases `Balance` by the `msg.value` but does not send funds back; the transaction itself sends that `msg.value` into the contract. Treat this as a code demonstration only.
11. Record gas used and transaction fee for deployment, deposit, and the balance-update call from transaction details.

## Expected observations

- Each wallet address has a separate balance.
- Only the deploying owner can deposit, withdraw/update the recorded balance, or read it.
- Solidity 0.8 checked arithmetic causes a withdrawal amount larger than `Balance` to revert due to underflow.
- This provided `Withdraw` does not transfer ETH out; the amount sent with the call goes into the contract.
- Deployment and state-changing calls consume gas; `showBalance` is a read-only call and normally does not create an on-chain transaction when called locally in Remix.

## Practical journal checklist

- Aim, tools, and the contract source code.
- Compiler version and test network.
- Contract address and deployment transaction hash.
- Deposit, balance before/after withdrawal, and over-withdrawal observation.
- Gas used and fee for deployment, deposit, and withdrawal.
- Screenshot of the deployed contract and successful calls. Do not show recovery phrases/private keys.

## Suggested conclusion

“I compiled and deployed a bank-account contract on Sepolia. It tracked balances per wallet, allowed deposits and valid withdrawals, and rejected withdrawals exceeding the account balance. I recorded gas usage for deployment and state-changing calls.”

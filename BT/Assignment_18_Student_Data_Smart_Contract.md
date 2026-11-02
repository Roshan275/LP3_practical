# Assignment 18 — Student data contract, fallback, gas, and fees

## Aim

Create and deploy a Solidity contract that stores student records in a struct array, includes a payable fallback, and lets you observe gas usage and transaction fees.

## What you need

- Browser access to [Remix IDE](https://remix.ethereum.org/).
- MetaMask connected to **Sepolia** with a small amount of Sepolia test ETH.
- Test ETH only; it has no real-world value.

## Solidity program

Use the provided [StudentData.sol](StudentData.sol) file. It stores student names and roll numbers in a dynamic array, rejects duplicate roll numbers, exposes list/index/count read functions, and includes payable `fallback` and `receive` handlers.

## Procedure in Remix

1. Open Remix IDE and create `StudentData.sol`. Copy the accompanying file's contents into Remix and save it.
2. In **Solidity Compiler**, choose compiler version `0.8.20` or a compatible `0.8.x`, then compile.
3. Open **Deploy & Run Transactions** and select the injected MetaMask provider. Confirm MetaMask is connected to Sepolia.
4. Select `StudentData` and click **Deploy**. Approve the testnet deployment in MetaMask.
5. After confirmation, record the deployed contract address, transaction hash, gas used, gas limit (if shown), gas price/effective gas price, and transaction fee.
6. Expand the deployed contract and call `addStudent` with sample values:
   - `name`: `Asha Patil`
   - `rollno`: `101`
7. Approve the transaction. Record its gas used and fee. Add a second record with a different roll number/name for comparison.
8. Call `getStudentCount`; it should return the number of records inserted. Call `getStudentByIndex(0)` to read the first record. You can also call `displayAllStudents`. These view calls are read-only when run locally in Remix.
9. To test `receive`, use MetaMask's send flow to send a small amount of Sepolia ETH to the deployed contract address with no data. Approve and record the transaction.
10. The supplied contract has no function that tracks the amount of Ether received. To check that the payable handler accepted a test transfer, inspect the contract's Sepolia address in a block explorer. If you want a storage-based balance getter, that would require changing the supplied contract; do not assume `displayAllStudents` reports Ether.
11. To test `fallback`, use Remix's low-level interaction area to send a small test value with non-empty unmatched calldata, if available. Otherwise, document the `receive` transaction and the fallback handler in your journal.
12. Open transaction details and record gas used and transaction fee for deployment, adding a student, and sending ETH. Fee is approximately `gas used × effective gas price`; convert Gwei to ETH by dividing Gwei by `1,000,000,000`.

## Expected observations

- Student records are appended to a dynamic array and can be read by index.
- `studentCount` increases after each successful `addStudent` transaction.
- `receive` accepts a plain ETH transfer; `fallback` handles unmatched function data and can accept ETH. The provided contract does not keep an accounting variable for the received amount.
- Deployment generally uses more gas than a single student insertion, but actual gas and fee depend on compiler settings, transaction data, and network conditions.

## Practical journal checklist

- Aim, tools, Solidity source, and compiler version.
- Network and deployed contract address.
- Two inserted student records and readback output.
- Deployment and insertion gas/fee measurements.
- Receive/fallback test and observed `etherReceived` value.
- Transaction hashes and screenshots of Remix/MetaMask transaction details. Hide private credentials.

## Suggested conclusion

“I used a struct and dynamic array to store and retrieve student data, and implemented payable receive/fallback handlers. I deployed on Sepolia and compared gas usage and transaction fees for deployment, data insertion, and Ether transfer.”

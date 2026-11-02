// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Bank {
    uint256 Balance=0;
    address public accOwner;

    constructor() {
        accOwner = msg.sender;
    }

    //deposit
    function Deposit() public payable {
        require(accOwner == msg.sender, "You are not the account Owner");
        require(msg.value > 0, "depositing value should be greater than 0");
        Balance+=msg.value;
    }

    //withdraw
    function Withdraw() public payable {
        require(accOwner == msg.sender, "You are not the account Owner");
        require(msg.value > 0, "withdrawal value should be greater than 0");
        Balance-=msg.value;
    }

    //showbalance
    function showBalance() public view returns(uint256) {
        require(accOwner == msg.sender, "You are not the account Owner");
        return Balance;
    }
}

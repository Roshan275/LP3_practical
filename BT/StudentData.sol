// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract StudentData {

    //structure
    struct Student {
        string name;
        uint rollno;
    }

    // array
    Student[] public studentarr;

    function addStudent(string memory name, uint rollno) public {
        for(uint i=0; i<studentarr.length; i++) {
            if(studentarr[i].rollno == rollno) {
                revert("Student roll no already exist");
            }
        }
        studentarr.push(Student(name, rollno));
    }

    function displayAllStudents() public view returns(Student[] memory) {
        return studentarr;
    }

    function getStudentByIndex(uint idx) public view returns(Student memory) {
        require(idx < studentarr.length, "index out of bound");
        return studentarr[idx];
    }

    function getStudentCount() public view returns(uint) {
        return studentarr.length;
    }

    fallback() external payable {
        //This fuction will handle external function calls that are not included in the contract
    }

    receive() external payable {
        //this function will handle ether sent by external user but without data mentioned.
    }
}

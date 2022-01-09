"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", (_) => {
  inputString = inputString
    .trim()
    .split("\n")
    .map((string) => {
      return string.trim();
    });

  main();
});

function readline() {
  return inputString[currentLine++];
}
// Make a Snippet for the code above this and then write your logic in main();

const getSpyIndex = (arrNum) => {
  // console.log("input string", arrNum);

  if (arrNum[0] === arrNum[2] && arrNum[1] !== arrNum[2]) {
    return 1;
  }
  for (let i = 2; i < arrNum.length; i++) {
    if (arrNum[0] !== arrNum[i]) {
      if (arrNum[1] === arrNum[i]) {
        return 0;
      } else {
        return i;
      }
    }
  }
};

function main() {
  const numberOfTestCases = 1 * readline();
  // console.log("number of test cases", numberOfTestCases);
  Array.from({ length: numberOfTestCases }).forEach(() => {
    const arrayLength = 1 * readline();
    const arrayString = readline();
    const arr = arrayString.split(" ");
    const arrNum = arr.map((x) => +x);

    console.log(getSpyIndex(arrNum) + 1);
  });
}

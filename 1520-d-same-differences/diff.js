"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", () => {
  inputString = inputString
    .trim()
    .split("\n")
    .map((string) => string.trim());

  main();
});

const readline = () => inputString[currentLine++];

// main logic

const main = () => {
  const numberOfTestCases = 1 * readline();
  // console.log("number of test cases", numberOfTestCases);
  Array.from({ length: numberOfTestCases }).forEach(() => {
    const arrayLength = 1 * readline();
    const arrayString = readline();
    const array = arrayString.split(" ");
    const arrayNum = array.map((x) => +x);

    // console.log(arrayNum);

    const map = new Map();
    let result = 0;
    for (let i = 0; i < arrayNum.length; i++) {
      const key = arrayNum[i] - i - 1;
      const current = map.get(key) || 0;
      result += current;
      map.set(key, current + 1);
    }
    console.log(result);
  });
};

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

const getCounter = (weightsArray) => {
  const mapping = new Map();

  weightsArray.forEach((weight) => {
    const currentCount = mapping.get(weight) || 0;
    mapping.set(weight, 1 + currentCount);
  });

  return mapping;
};

const main = () => {
  const numberOfTestCases = 1 * readline();
  // console.log("number of test cases", numberOfTestCases);
  Array.from({ length: numberOfTestCases }).forEach(() => {
    const arrayLength = 1 * readline();
    const arrayString = readline();
    const array = arrayString.split(" ");
    const arrayNum = array.map((x) => +x);

    // console.log(arrayNum);
    const mapping = Array.from(
      { length: 1 + 2 * Math.max(...arrayNum) },
      () => 0
    );

    const weightsCounter = getCounter(arrayNum);

    // console.log(weightsCounter);

    for (const [first, firstCount] of weightsCounter) {
      for (const [second, secondCount] of weightsCounter) {
        mapping[first + second] += Math.min(firstCount, secondCount);
      }
    }

    // console.log(mapping);

    const pairsCount = Math.floor(Math.max(...mapping) / 2);
    console.log(pairsCount);
  });
};

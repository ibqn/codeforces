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

const countPair = (weightsList, weight) => {
  for (let first = 0; first < weightsList.length; first++) {
    for (let second = first + 1; second < weightsList.length; second++) {
      const currentWeight = weightsList[first] + weightsList[second];
      if (currentWeight === weight) {
        const newList = weightsList
          .slice(0, first)
          .concat(weightsList.slice(first + 1, second))
          .concat(weightsList.slice(second + 1));
        return 1 + countPair(newList, weight);
      }
    }
  }
  return 0;
};

const weightCounts = (weights) => {
  let pairCount = 0;
  const weightPair = new Set();

  for (let first = 0; first < weights.length; first++) {
    for (let second = first + 1; second < weights.length; second++) {
      const sum = weights[first] + weights[second];
      weightPair.add(sum);
    }
  }

  for (let s of weightPair) {
    pairCount = Math.max(pairCount, countPair(weights, s));
  }
  return pairCount;
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
    console.log(weightCounts(arrayNum));
  });
};

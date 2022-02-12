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

//  Write your logic in `main`

const reverse = (palindrome) => palindrome.split("").reverse().join("");

const makePalindrome = (palindrome, counts) => {
  let newPalindrome = "";
  for (let i = 0; i < Math.ceil(palindrome.length / 2); i++) {
    let left = palindrome[i];
    let right = palindrome[palindrome.length - 1 - i];

    if (left !== right && left !== "?" && right !== "?") {
      // console.log("error: no match");
      return -1;
    }

    let character = left;

    if (left === "?") {
      left = right;
      character = right;
    }

    if (right === "?") {
      right = left;
      character = left;
    }

    newPalindrome += character;

    counts[left] -= 1;
    if (i !== palindrome.length - 1 - i) {
      counts[right] -= 1;
    }
  }

  if (counts["0"] < 0 || counts["1"] < 0) {
    return -1;
  }

  if (counts["?"] % 2 === 0) {
    if (counts["0"] % 2 !== 0 || counts["1"] % 2 !== 0) {
      // console.log("error: not even");
      return -1;
    }
  }

  counts["?"] += counts["1"] + counts["0"];

  if (counts["?"] !== 0) {
    // console.log("error: not zero");
    return -1;
  }

  // console.log("looks good");

  // console.log("new", newPalindrome, counts);
  newPalindrome = newPalindrome
    .split("")
    .map((el) => {
      if (el === "?") {
        // console.log("map", counts);
        if (counts["0"] > 1) {
          counts["0"] -= 2;
          return "0";
        } else if (counts["1"] > 1) {
          counts["1"] -= 2;
          return "1";
        }

        // for a single question mark in the case with odd palindrome length
        if (counts["0"] > 0) {
          return "0";
        } else {
          return "1";
        }
      }
      return el;
    })
    .join("");

  return (
    newPalindrome +
    reverse(newPalindrome.slice(0, Math.floor(palindrome.length / 2)))
  );
};

const main = () => {
  const numberOfTestCases = 1 * readline();
  // console.log("number of test cases", numberOfTestCases);

  Array.from({ length: numberOfTestCases }).forEach(() => {
    const [zerosCount, onesCount] = readline()
      .split(" ")
      .map((el) => +el);

    // console.log(zerosCount, onesCount);

    const palindrome = readline();

    // console.log(palindrome);

    const counts = {
      0: zerosCount,
      1: onesCount,
      "?": 0,
    };

    console.log(makePalindrome(palindrome, counts));
  });
};

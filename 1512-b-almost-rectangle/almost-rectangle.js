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
// Make a Snippet for the code above and then write your logic in `main`

const makeSquareArray = (squareLength) => {
  const squareString = [];

  Array.from({ length: squareLength }).forEach(() => {
    const stringArray = readline().split("");
    squareString.push(stringArray);
  });

  return squareString;
};

const getCoordinates = (squareString) => {
  const cellCoords = [];
  for (let x = 0; x < squareString.length; x++) {
    const row = squareString[x];
    for (let y = 0; y < row.length; y++) {
      if (row[y] === "*") {
        cellCoords.push({ x, y });
      }
      if (cellCoords.length === 2) {
        return cellCoords;
      }
    }
  }
};

const normalizeSet = (coordsSet) => {
  if (coordsSet.size === 1) {
    coordsSet.add(0);
  }

  if (coordsSet.size === 1) {
    coordsSet.add(1);
  }

  return coordsSet;
};

const main = () => {
  const numberOfTestCases = 1 * readline();
  // console.log("number of test cases", numberOfTestCases);

  Array.from({ length: numberOfTestCases }).forEach(() => {
    const squareLength = 1 * readline();

    let squareString = makeSquareArray(squareLength);

    const [pointOne, pointTwo] = getCoordinates(squareString);
    // console.log("cells", coords);

    let xSet = new Set();
    xSet.add(Math.min(pointOne.x, pointTwo.x));
    xSet.add(Math.max(pointOne.x, pointTwo.x));
    xSet = normalizeSet(xSet);

    let ySet = new Set();
    ySet.add(Math.min(pointOne.y, pointTwo.y));
    ySet.add(Math.max(pointOne.y, pointTwo.y));
    ySet = normalizeSet(ySet);

    for (let x of xSet) {
      for (let y of ySet) {
        squareString[x][y] = "*";
      }
    }

    // console.log(squareString);
    squareString.forEach((line) => {
      console.log(line.join(""));
    });
  });
};

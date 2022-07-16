function create2DArray(length) {
  if (!length) return [[]];
  const size = parseInt(length / 2);
  const array = [];
  for (let i = 0; i < size; i++) {
    const subArray = [];
    for (let j = 0; j < size; j++) {
      subArray[j] = 0;
    }
    array.push(subArray);
  }
  return array;
}

function maxValue(matrix) {
  if (!matrix) return 0;
  if (!matrix[0]) return 0;
  const n = matrix[0].length;
  const topLeftArea = create2DArray(n);
  let maxValue = 0;
  for (let i = 0; i < topLeftArea.length; i++) {
    for (let j = 0; j < topLeftArea[0].length; j++) {
      topLeftArea[i][j] = Math.max(
        matrix[i][j],
        matrix[i][n - 1 - j],
        matrix[n - 1 - i][j],
        matrix[n - 1 - i][n - 1 - j],
      );
    }
  }
  for (let i = 0; i < topLeftArea.length; i++) {
    for (let j = 0; j < topLeftArea.length; j++) {
      maxValue += topLeftArea[i][j];
    }
  }

  return maxValue;
}

const matrix = [
  [112, 42, 83, 119],
  [56, 125, 56, 49],
  [15, 78, 101, 43],
  [62, 98, 114, 108],
];
console.log(maxValue(matrix));

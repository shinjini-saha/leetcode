export function trapRainWater(heightMap: number[][]): number {
  const numRows = heightMap.length;
  if (numRows <= 2) {
    return 0;
  }
  const numColumns = heightMap[0]!.length;
  if (numColumns <= 2) {
    return 0;
  }

  const collection: number[][] = [];

  for (let r = 0; r < numRows; r++) {
    const row: number[] = [];
    collection.push(row);
    for (let c = 0; c < numColumns; c++) {
      if (r === 0 || r === numRows - 1 || c === 0 || c === numColumns - 1) {
        row.push(heightMap[r]![c]!);
        continue;
      }
      row.push(Number.POSITIVE_INFINITY);
    }
  }

  let done = false;
  while (!done) {
    let isFinalRound = true;
    for (let r = 0; r < numRows; r++) {
      for (let c = 0; c < numColumns; c++) {
        const cellDone = processCell(r, c, heightMap, collection);
        if (!cellDone) {
          isFinalRound = false;
        }
      }
    }
    if (isFinalRound) {
      done = true;
    }
  }

  let waterCollected = 0;
  for (let r = 0; r < numRows; r++) {
    for (let c = 0; c < numColumns; c++) {
      waterCollected += collection[r]![c]! - heightMap[r]![c]!;
    }
  }

  return waterCollected;
}

function processCell(r: number, c: number, heightMap: number[][], collection: number[][]): boolean {
  const numRows = heightMap.length;
  const numColumns = heightMap[0]!.length;

  if (r === 0 || r === numRows - 1) {
    return true;
  }
  if (c === 0 || c === numColumns - 1) {
    return true;
  }

  const h = heightMap[r]![c]!;
  const oldC = collection[r]![c]!;

  const topC = collection[r - 1]![c]!;
  const bottomC = collection[r + 1]![c]!;
  const leftC = collection[r]![c - 1]!;
  const rightC = collection[r]![c + 1]!;

  const newC = Math.max(h, Math.min(topC, bottomC, leftC, rightC));

  collection[r]![c] = newC;

  return oldC === newC;
}

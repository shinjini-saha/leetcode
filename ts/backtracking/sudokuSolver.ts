/**
 Do not return anything, modify board in-place instead.
 */

type SudokuCache = Array<Array<Set<string>>>;
type Key = `${number},${number}`;

export function solveSudoku(board: string[][]): void {
  const staticIndices = getStaticIndices(board);
  const cache: SudokuCache = fillCache(board, staticIndices);
  solveSudokuHelper(board, cache, staticIndices, new Set());
}

function solveSudokuHelper(
  board: string[][],
  cache: SudokuCache,
  staticIndices: Set<Key>,
  seen: Set<Key>,
): boolean {
  const { min, isWin } = getNextRowCol(board, cache);
  if (isWin) {
    return true;
  }
  if (min == null) {
    return false;
  }
  const { row, col } = min;

  const validNumbers = [...cache[row]![col]!];

  const key = getKey(row, col);
  seen.add(key);
  for (const n of validNumbers) {
    board[row]![col] = n;
    const delta = removeFromCache(row, col, n, cache, staticIndices);
    const solved = solveSudokuHelper(board, cache, staticIndices, seen);
    if (solved) {
      return solved;
    }
    board[row]![col] = '.';

    restoreCache(n, delta, cache);
  }
  seen.delete(key);
  return false;
}

const VALID_VALUES = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];

function getValidRowNumbers(board: string[][], row: number) {
  const validNumbers = new Set<string>(VALID_VALUES);
  for (const n of board[row]!) {
    if (n === '.') {
      continue;
    }
    validNumbers.delete(n);
    if (validNumbers.size === 0) {
      return validNumbers;
    }
  }
  return validNumbers;
}

function getValidColNumbers(board: string[][], col: number) {
  const validNumbers = new Set<string>(VALID_VALUES);
  for (let i = 0; i < 9; i++) {
    const n = board[i]![col]!;
    if (n === '.') {
      continue;
    }
    validNumbers.delete(n);
    if (validNumbers.size === 0) {
      return validNumbers;
    }
  }
  return validNumbers;
}

function getValidSquareNumbers(board: string[][], row: number, col: number) {
  const validNumbers = new Set<string>(VALID_VALUES);

  forSquare(row, col, (r, c) => {
    const n = board[r]![c]!;
    if (n === '.') {
      return false;
    }
    validNumbers.delete(n);
    if (validNumbers.size === 0) {
      return true;
    }
    return false;
  });
  return validNumbers;
}

function getNextRowCol(
  board: string[][],
  cache: SudokuCache,
): { min: { row: number; col: number }; isWin: false } | { min: null; isWin: boolean } {
  let min: { size: number; row: number; col: number } | null = null;
  let anyEmpty = false;
  for (let row = 0; row < 9; row++) {
    for (let col = 0; col < 9; col++) {
      const n = board[row]![col]!;
      if (n !== '.') {
        continue;
      }
      anyEmpty = true;
      const validNumbers = cache[row]![col]!;
      const size = validNumbers.size;
      if (size === 0) {
        continue;
      }
      if (min == null || size < min.size) {
        min = { size, row, col };
      }
    }
  }
  if (min !== null) {
    return { min, isWin: false };
  }
  return { min: null, isWin: !anyEmpty };
}

function getStaticIndices(board: string[][]): Set<Key> {
  const staticIndices = new Set<Key>();
  for (let row = 0; row < 9; row++) {
    for (let col = 0; col < 9; col++) {
      const n = board[row]![col]!;
      if (n !== '.') {
        staticIndices.add(getKey(row, col));
      }
    }
  }
  return staticIndices;
}

function getKey(row: number, col: number): Key {
  return `${row},${col}`;
}

function fillCache(board: string[][], staticIndices: Set<string>) {
  const cache: SudokuCache = [];
  for (let row = 0; row < 9; row++) {
    const rows = [];
    for (let col = 0; col < 9; col++) {
      const key = getKey(row, col);
      const validNumbers = new Set<string>();

      if (staticIndices.has(key)) {
        rows.push(validNumbers);
        continue;
      }

      const validRowNumbers = getValidRowNumbers(board, row);
      const validColNumbers = getValidColNumbers(board, col);
      const validSquareNumbers = getValidSquareNumbers(board, row, col);

      for (const n of VALID_VALUES) {
        if (validRowNumbers.has(n) && validColNumbers.has(n) && validSquareNumbers.has(n)) {
          validNumbers.add(n);
        }
      }

      rows.push(validNumbers);
    }
    cache.push(rows);
  }

  return cache;
}

function restoreCache(value: string, delta: Record<string, boolean>, cache: SudokuCache) {
  for (const key in delta) {
    if (!delta[key]) {
      continue;
    }
    const [rowStr, colStr] = key.split(',') as [string, string];
    const row = parseInt(rowStr);
    const col = parseInt(colStr);
    cache[row]![col]!.add(value);
  }
}

function removeFromCache(
  row: number,
  col: number,
  value: string,
  cache: SudokuCache,
  staticIndices: Set<string>,
) {
  const delta: Record<string, boolean> = {};
  for (let r = 0; r < 9; r++) {
    const key = getKey(r, col);
    if (staticIndices.has(key)) {
      continue;
    }
    const removed = cache[r]![col]!.delete(value);
    if (removed) {
      delta[key] = true;
    }
  }
  for (let c = 0; c < 9; c++) {
    const key = getKey(row, c);
    if (staticIndices.has(key)) {
      continue;
    }
    const removed = cache[row]![c]!.delete(value);
    if (removed) {
      delta[key] = true;
    }
  }
  forSquare(row, col, (r, c) => {
    const key = getKey(r, c);
    if (staticIndices.has(key)) {
      return false;
    }
    const removed = cache[r]![c]!.delete(value);
    if (removed) {
      delta[key] = true;
    }
    return false;
  });

  return delta;
}

function forSquare(row: number, col: number, handler: (r: number, c: number) => boolean) {
  const baseRowIdx = Math.floor(row / 3) * 3;
  const baseColIdx = Math.floor(col / 3) * 3;
  for (let i = 0; i < 3; i++) {
    const r = baseRowIdx + i;
    for (let j = 0; j < 3; j++) {
      const c = baseColIdx + j;
      const shouldStop = handler(r, c);
      if (shouldStop) {
        return;
      }
    }
  }
}

// eslint-disable-next-line @typescript-eslint/no-unused-vars
function prettyPrintBoard(board: string[][]) {
  let boardStr = '';
  for (let r = 0; r < 9; r++) {
    let rowStr = '';
    if (r % 3 === 0) {
      for (let c = 0; c < 9 + 4; c++) {
        boardStr += '_';
      }
      boardStr += '\n';
    }
    for (let c = 0; c < 9; c++) {
      const n = board[r]![c]!;
      if (c % 3 === 0) {
        rowStr += '|';
      }
      rowStr += n;
    }
    rowStr += '|\n';
    boardStr += rowStr;
  }
  for (let c = 0; c < 9 + 4; c++) {
    boardStr += '_';
  }

  // eslint-disable-next-line no-console
  console.log(boardStr);
}

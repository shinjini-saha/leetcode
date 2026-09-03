import { trapRainWater } from '../trapRainWater2.js';

describe('trapRainWater', () => {
  it('is correct', () => {
    let heightMap = [
      [1, 4, 3, 1, 3, 2],
      [3, 2, 1, 3, 2, 4],
      [2, 3, 3, 2, 3, 1],
    ]; // 4

    expect(trapRainWater(heightMap)).toBe(4);

    heightMap = [
      [3, 3, 3, 3, 3],
      [3, 2, 2, 2, 3],
      [3, 2, 1, 2, 3],
      [3, 2, 2, 2, 3],
      [3, 3, 3, 3, 3],
    ]; // 10

    expect(trapRainWater(heightMap)).toBe(10);

    heightMap = [
      [12, 13, 1, 12],
      [13, 4, 13, 12],
      [13, 8, 10, 12],
      [12, 13, 12, 12],
      [13, 13, 13, 13],
    ]; // 14

    expect(trapRainWater(heightMap)).toBe(14);
  });
});

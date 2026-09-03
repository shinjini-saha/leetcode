import { trap } from '../trapRainWater.js';

describe('trap', () => {
  it('is correct', () => {
    let height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]; // 6
    expect(trap(height)).toBe(6);

    height = [4, 2, 0, 3, 2, 5]; // 9
    expect(trap(height)).toBe(9);

    height = [2, 0, 2]; // 2
    expect(trap(height)).toBe(2);
  });
});

import { firstMissingPositive } from '../firstMissingPosInt.js';

describe('firstMissingPositive', () => {
  it('is correct', () => {
    let nums = [1, 2, 0];
    expect(firstMissingPositive(nums)).toEqual(3);

    nums = [3, 4, -1, 1];
    expect(firstMissingPositive(nums)).toEqual(2);

    nums = [7, 8, 9, 11, 12];
    expect(firstMissingPositive(nums)).toEqual(1);

    nums = [8, 9, 11, 12, 7];
    expect(firstMissingPositive(nums)).toEqual(1);

    nums = [1];
    expect(firstMissingPositive(nums)).toEqual(2);

    nums = [100000, 3, 4000, 2, 15, 1, 99999];
    expect(firstMissingPositive(nums)).toEqual(4);

    nums = [1, 1];
    expect(firstMissingPositive(nums)).toEqual(2);
  });
});

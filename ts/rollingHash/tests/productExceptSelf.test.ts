import { productExceptSelf } from '../productExceptSelf.js';

describe('productExceptSelf', () => {
  it('is correct', () => {
    let nums = [1, 2, 3, 4];
    expect(productExceptSelf(nums)).toEqual([24, 12, 8, 6]);

    nums = [-1, 1, 0, -3, 3];
    expect(productExceptSelf(nums)).toEqual([0, 0, 9, 0, 0]);
  });
});

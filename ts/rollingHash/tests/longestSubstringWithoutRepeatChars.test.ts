import { lengthOfLongestSubstring } from '../longestSubstringWithoutRepeatChars.js';

describe('lengthOfLongestSubstring', () => {
  it('is correct', () => {
    expect(lengthOfLongestSubstring(' ')).toEqual(1);
    expect(lengthOfLongestSubstring('pwwkew')).toEqual(3);
  });
});

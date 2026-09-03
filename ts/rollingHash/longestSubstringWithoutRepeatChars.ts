export function lengthOfLongestSubstring(s: string): number {
  if (s.length === 0) {
    return 0;
  }

  let startIdx = 0;
  let endIdx = 0;
  const charBag = new Set();
  let maxLength = 0;

  while (endIdx < s.length) {
    const nextChar = s[endIdx];
    while (charBag.has(nextChar)) {
      const startChar = s[startIdx];
      charBag.delete(startChar);
      startIdx++;
    }
    charBag.add(nextChar);
    if (charBag.size > maxLength) {
      maxLength = charBag.size;
    }

    endIdx++;
  }

  return maxLength;
}

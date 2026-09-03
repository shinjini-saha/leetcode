export function firstMissingPositive(nums: number[]): number {
  const len = nums.length;
  let i = len - 1;
  while (i >= 0) {
    const n = nums[i]!;
    if (n > i || n <= 0) {
      i -= 1;
      continue;
    }
    // Swap
    const old = nums[n - 1]!;
    if (old === n) {
      nums[i] = Number.POSITIVE_INFINITY;
      i -= 1;
      continue;
    }
    nums[n - 1] = n;
    nums[i] = old;

    if (old > i || old <= 0) {
      i -= 1;
    }
  }

  let last = 0;
  for (const n of nums) {
    if (n === last + 1) {
      last = n;
    } else {
      return last + 1;
    }
  }

  return last + 1;
}

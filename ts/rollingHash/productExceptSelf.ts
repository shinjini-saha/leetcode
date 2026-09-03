export function productExceptSelf(nums: number[]): number[] {
  const len = nums.length;
  const productForward = new Array(len);
  const productBackward = new Array(len);

  let forward = 1;
  let backward = 1;
  for (let i = 0; i < len; i++) {
    forward = forward * nums[i]!;
    productForward[i] = forward;
    const j = len - 1 - i;
    backward = backward * nums[j]!;
    productBackward[j] = backward;
  }

  const res = [];
  for (let i = 0; i < len; i++) {
    const f = i === 0 ? 1 : productForward[i - 1];
    const b = i === len - 1 ? 1 : productBackward[i + 1];

    const prod = f * b;
    if (prod === 0) {
      res.push(0);
    } else {
      res.push(prod);
    }
  }

  return res;
}

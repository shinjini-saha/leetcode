export function trap(height: number[]): number {
  if (height.length <= 2) {
    return 0;
  }

  let startIndex = 0;
  let startHeight = height[startIndex]!;
  let endIndex = height.length - 1;
  let endHeight = height[endIndex]!;

  let waterCollected = 0;
  while (startIndex < endIndex) {
    if (startHeight <= endHeight) {
      startIndex += 1;
      const newStartHeight = height[startIndex]!;
      if (newStartHeight >= startHeight) {
        startHeight = newStartHeight;
      } else {
        const diff = Math.min(startHeight, endHeight) - newStartHeight;
        waterCollected += diff;
      }
    } else {
      endIndex -= 1;
      const newEndHeight = height[endIndex]!;
      if (newEndHeight >= endHeight) {
        endHeight = newEndHeight;
      } else {
        const diff = Math.min(startHeight, endHeight) - newEndHeight;
        waterCollected += diff;
      }
    }
  }

  return waterCollected;
}

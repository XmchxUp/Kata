function cutCube(volume, n) {
  //coding here...
  if (!Number.isInteger(Math.cbrt(n))) {
    return false;
  }
  let oneCubeVolume = volume / n;
  if (!Number.isInteger(oneCubeVolume)) {
    return false;
  }
  return Number.isInteger(Math.cbrt(oneCubeVolume));
}

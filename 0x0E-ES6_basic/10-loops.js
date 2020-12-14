export default function appendToEachArrayValue(array, appendString) {
  const newArr = [];
  for (const val of array) {
    const newVal = appendString + val;
    newArr.push(newVal);
  }

  return newArr;
}

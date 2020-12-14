export default function createIteratorObject(report) {
  let array = [];
  for (const val of Object.values(report.allEmployees)) {
    array = [...array, ...val];
  }
  return array;
}

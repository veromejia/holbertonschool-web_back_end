export default function groceriesList() {
  const groceries = new Map();
  groceries.set('Apples', 10)
    .set('Tomatoes', 10)
    .set('Pasta', 1)
    .set('Rice', 1)
    .set('Banana', 5);
  return groceries;
}

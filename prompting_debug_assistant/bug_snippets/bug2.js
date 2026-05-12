/**
 * Bug 2 - bug2.js
 * Intended Behavior: Apply a tiered discount to a shopping cart total.
 *   >= $200 -> 20% off
 *   >= $100 -> 10% off
 *   Otherwise -> 0% off
 * Issue Type: Logical error (wrong condition order)
 */

function applyDiscount(total) {
  let discount = 0;

  if (total >= 100) {
    discount = 0.10;
  } else if (total >= 200) {
    discount = 0.20;
  }

  const discountAmount = total * discount;
  const finalPrice = total - discountAmount;
  return parseFloat(finalPrice.toFixed(2));
}

console.log(applyDiscount(50));
console.log(applyDiscount(150));
console.log(applyDiscount(250));
console.log(applyDiscount(100));
console.log(applyDiscount(200));

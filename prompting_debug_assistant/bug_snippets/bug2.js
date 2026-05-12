/**
 * Bug 2 - bug2.js
 * Intended Behavior: Apply a tiered discount to a shopping cart total.
 *   Purchases >= $200 receive 20% off.
 *   Purchases >= $100 receive 10% off.
 *   Purchases below $100 receive no discount.
 * Issue Type: Logical error (wrong condition order).
 * Notes: Conditions are evaluated smallest-first. Any total >= 200 also
 *        satisfies >= 100, so the 20% branch is dead/unreachable code.
 *        Customers spending $200+ only ever receive 10% off instead of 20%.
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

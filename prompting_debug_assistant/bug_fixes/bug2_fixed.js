/**
 * Bug 2 - bug2_fixed.js
 * Fix: Swapped condition order — check >= 200 before >= 100.
 */

function applyDiscount(total) {
  let discount = 0;
  if (total >= 200) {
    discount = 0.20;
  } else if (total >= 100) {
    discount = 0.10;
  }
  const discountAmount = total * discount;
  const finalPrice = total - discountAmount;
  return parseFloat(finalPrice.toFixed(2));
}

console.assert(applyDiscount(50)  === 50,  "Test 1 failed");
console.assert(applyDiscount(100) === 90,  "Test 2 failed");
console.assert(applyDiscount(150) === 135, "Test 3 failed");
console.assert(applyDiscount(200) === 160, "Test 4 failed");
console.assert(applyDiscount(250) === 200, "Test 5 failed");
console.log("All tests passed!");

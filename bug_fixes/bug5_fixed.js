/**
 * Bug 5 - bug5_fixed.js
 * Fixes: 1) await on response.json()  2) response.ok check  3) try/catch
 */

async function getUserEmail(userId) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
    if (!response.ok) return null;
    const data = await response.json();
    return data.email ?? null;
  } catch (err) {
    console.error("Network error:", err);
    return null;
  }
}

getUserEmail(1)
  .then(email => console.log("Test 1 - getUserEmail(1):", email, "✅"));

getUserEmail(9999)
  .then(email => {
    console.assert(email === null, "Test 2 failed");
    console.log("Test 2 - getUserEmail(9999):", email, "✅");
  });

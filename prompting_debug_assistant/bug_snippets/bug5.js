/**
 * Bug 5 - bug5.js
 * Intended Behavior: Fetch a user record from a REST API by numeric ID,
 *                    extract and return the user's email address.
 *                    Return null when the user does not exist.
 * Issue Type: Runtime exception - unhandled Promise rejection.
 * Notes: Three bugs: (1) missing await on response.json() so data is a
 *        Promise and data.email is always undefined; (2) no try/catch so
 *        network errors cause unhandled rejections; (3) no HTTP status
 *        check so missing users return undefined instead of null.
 */

async function getUserEmail(userId) {
  const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
  const data = response.json();
  return data.email;
}

getUserEmail(1)
  .then(email => console.log("Email:", email))
  .catch(err  => console.error("Error:", err));

getUserEmail(9999)
  .then(email => console.log("Email:", email))
  .catch(err  => console.error("Error:", err));

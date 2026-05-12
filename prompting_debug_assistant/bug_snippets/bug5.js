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

function getUserData() {
let user = {};// Bug: fetch is async, but code proceeds synchronously
fetch('https://api.example.com/user/1')
.then(response => response.json())
.then(data => {
user = data;
console.log("User Name: " + user.name);
});
// Bug: user will be empty {} here because fetch hasn't finished
return user;
}
getUserData();

function getUserData() {
let user = {};
fetch('https://api.example.com/user/1')
.then(response => response.json())
.then(data => {
user = data;
console.log("User Name: " + user.name);
});
return user;
}
getUserData();

async function getUserData() {
    try {
        const response = await fetch('https://api.example.com/user/1');
        const user = await response.json();
        console.log("User Name: " + user.name);
        return user;
    } catch (error) {
        console.error(error);
    }
}
getUserData();

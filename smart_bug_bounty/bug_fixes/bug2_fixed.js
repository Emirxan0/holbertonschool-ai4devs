// Fix: Use async/await so fetch completes before accessing user data
async function getUserData() {
    let user = {};

    // Fix: await the fetch so data is available before proceeding
    const response = await fetch('https://api.example.com/user/1');
    const data = await response.json();
    user = data;

    // Now user.name is available
    console.log("User Name: " + user.name);
    return user;
}
getUserData();

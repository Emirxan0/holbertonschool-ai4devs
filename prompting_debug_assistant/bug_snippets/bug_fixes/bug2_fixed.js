function validateUser(user) {
    if (user.age < 18) {
        return false;
    }

    let minLength = 8;
    if (user.password.length < minLength) { 
        return false;
    }

    if (user.role === "admin") { 
        return true;
    }
    return true;
}

const myUser = { name: "Emir", age: 20, password: "secure123", role: "user" };
console.log(validateUser(myUser));

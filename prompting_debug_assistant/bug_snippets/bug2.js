function validateUser(user) {
    if (user.age < 18 {
        return false;
    }

    let minLength = 8;
    if (user.password.length < minLenght) { 
        return false;
    }

    if (user.role = "admin") { 
        return true;
    }
    return true;
}

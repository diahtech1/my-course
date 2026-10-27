"use strict";
function birthYear(name, year) {
    const defaultyear = 2026;
    if (!name) {
        return ("enter your name");
    }
    if (year > defaultyear) {
        return ("birth year cannot be greater than 2026");
    }
    let userAge = (defaultyear - year);
    return `Welcome! ${name}. You are ${userAge} years old`;
}
const result = birthYear("Josiah", 2023);
console.log(result);

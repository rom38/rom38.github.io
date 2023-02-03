// Задание 3.
// Написать функцию, которая создает
// пустой объект, но без прототипа.

function emptyObj() {
    // return {}
    return Object()
}
console.log(emptyObj())

console.log(Object.getPrototypeOf(emptyObj()))
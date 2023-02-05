function getTypeOfNumbers() {
    const arr = [0, null, NaN, 0, 1, 2, 4, "str"]

    let even = 0,
        odd = 0,
        zero = 0;

    for (let i = 0; i < arr.length; i++) {
        if (typeof arr[i] === 'number' && !isNaN(arr[i])) {
            if (arr[i] === 0) {
                zero += 1;
            } else if (arr[i] % 2 === 0) {
                even += 1;
            } else {
                odd += 1;
            }
        }
    }
    console.log('четных элементов: ', even)
    console.log('нечетных элементов: ', odd)
    console.log('нулей: ', zero)
}


function isPrime(num) {
    if (num > 1000){
        console.log(`number is bigger than 1000 -  ${num}`)
        return undefined
    }
    if (num<=1){
        return false
    }
    if (num<=3){
        return true
    }
    if ((num % 2) === 0 | (num % 3) === 0 ){
        return false
    }
    intSqrt = Math.floor(Math.sqrt(num))
    for (i = 5; i < (intSqrt+1); i = i + 2){
        if ((num % i) === 0){
            return false
        }
    }
    return true
}

function sum_ab (num_a){
    return function(num_b){
        return num_a+num_b
    }


}



//getTypeOfNumbers()

//console.log( isPrime(998))

console.log(sum_ab(5)(7))

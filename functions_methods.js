//Functions & Methods JS:-

//function myFunction() {
//    console.log("Hello khushi")
//    console.log("How are you?")
//}
//myFunction();

//function myFunction(msg) {
//    //parameter input
//    console.log(msg)
//}
//myFunction("I Love JS.") // argument

//Function -> 2 numbers of sum
//function sum(a ,b) {
//    console.log(a + b);
//}

//function sum(x ,y) {
//    s = x + y;
//    return s;
//}
//let val = sum(3, 4);
//console.log(val);  //7

//Arrow function:-

//const arrowsum = (a, b) => {
//    console.log(a + b);
//};

//const arrowmul = (a, b) => {
//    console.log(a * b)
//}

//function countVowels(str) {
//    let count = 0;
//    for (const char of str) {
//        if(char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u') {
//            count++;
//        }
//    }
//    return count;
//}

//const countVow = (str) => {
//     let count = 0;
//    for (const char of str) {
//        if(char === 'a' ||
//           char === 'e' ||
//           char === 'i' ||
//           char === 'o' ||
//           char === 'u'
//           ) {
//            count++;
//        }
//    }
//    return count;
//}

//let arr = [1,2,3,4,5];
//
//arr.forEach((val) => {
//    console.log(val);
//});


//let cities = ["Junagadh","Rajkot","Ahmedabad"]
//
//cities.forEach((val) => {
//    console.log(val.toUpperCase());    //JUNAGADH RAJKOT AHMEDABAD
//});

//let num = [2,3,4,5,6];
//num.forEach((num) => {
//    console.log(num*num);  //4,9,16,25,36
//});

//let nums = [11,22,33,44,55];
//let newArr = nums.map((val) => {
//    return val * 2;
//});
//console.log(newArr)

//let arr = [1,2,3,4,5,6,7];
//let evenArr = arr.filter((val) => {
//    return val % 2 === 0;
//})
//console.log(evenArr)

//let arr = [1,2,3,4];
//
//const output = arr.reduce((prev, curr) => {
//    return prev + curr;
//});
//console.log(output);  //10

//let arr = [5,6,2,1,3];
//
//const output = arr.reduce((prev, curr) => {
//    return prev > curr ? prev : curr;
//})
//console.log(output)           //largest number

//let arr = [87,93,64,99,86];
//let result = arr.filter((val) => {
//    return val > 90;
//})
//console.log(result)  //[93, 99]

//let n = prompt("Enter a number : ")
//let arr = []
//for (let i=1; i<=n; i++ ){
//    arr[i-1] = i;
//}
//console.log(arr)
//let result = arr.reduce((sum,curr) => {
//    return sum + curr;
//})
//console.log(result)
//
//let Factorial = arr.reduce((sum,curr) => {
//    return sum * curr;
//})
//console.log(Factorial)

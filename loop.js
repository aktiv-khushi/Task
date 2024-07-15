//loop

//For loop:-
//Ex-1:-

//for (let i = 1; i <= 100; i++) {
//    console.log("Hello World");
//}

//Ex-2:-

//let sum = 0;
//for (let i = 1; i <=5; i++) {
//    sum = sum + i;
//}
//console.log("sum =",sum);

//For of loop:-

//Ex-3:-

//let str = "Hellokhushi"
//
//for (let i of str) {
//    console.log("i =",i)
//}

//Ex-4:-

//let student = {
//    name: "Khushi",
//    age: 21,
//    cgpa: 8.42,
//    isPass: true,
//};
//
//for (let key in student) {
//    console.log("key =",key, " value =",student[key])
//}

//Ex-5:-

//for (let num = 0; num <= 100; num++) {
//    if (num%2===0) {
//        console.log('num =',num)
//    }
//}

//Ex-6:-

//let game = 25;
//let userNum = prompt("Guess the game number: ");
//while(userNum != game) {
//   userNum = prompt("you enterd wrong number.Guess again");
//}
//console.log("congratulations , You entered the right number");

//String in JS:-.

//let str = "khushi";
//console.log(str[0]); //k
//let str1 = "aktivsoftware";
//let str2 = "icreative";

//str[1] //k //Terminal to run

//Template literals:-
//let specialString = `This is template literals ${1 + 2 + 3}`;
//console.log(specialString) //6

//console.log("icreative\nTechnologies") //Next line
//console.log("icreative\tTechnologies") //tab space

//let str = "khushi";
//let string = str.toUpperCase();
//console.log(string)

//let str = "KHUSHI";
//let string = str.toLowerCase();
//console.log(string)

//let str = "  KHUSHI  ";
//let string = str.trim()
//console.log(string)  //Remove white Space starting and ending.

//let string = "0123456";
//console.log(string.slice(1, 3))

//let string1 = "hello";
//let string2 = "khushi";
//let res = string1.concat(string2)
//console.log(res)   //join string1 with string2.

//let str = "hello";
//console.log(str.replace("h","y"));

//let name = prompt("enter a fullname:");
//let userName = "@" + name+ name.length;
//console.log(userName)


//1.Display Current Day and Time:
//Write a JavaScript program to display the current day and time in the following format.

const now = new Date();
const day = now.getDay();
const hours = now.getHours();
const minutes = now.getMinutes();
const seconds = now.getSeconds();
console.log(`Today is day ${day} and the time is ${hours}:${minutes}:${seconds}`);






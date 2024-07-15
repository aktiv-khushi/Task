
//3. Find 1st January Sunday:
//Write a JavaScript program to find out if 1st January will be a Sunday between 2014 and 2050.
   
for (let year = 2014;year<=2050;year++) {
    let date = new Date(year, 0 ,1); //January is month 0
    if (date.getDay() === 0) // 0 represents Sunday

console.log("1st January is being a sunday "+year);
}



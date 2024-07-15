//2. Get Current Date:
   //Write a JavaScript program to get the current date.
   //- Expected Output:
     //- `mm-dd-yyyy`, `mm/dd/yyyy`
     //- `dd-mm-yyyy`, `dd/mm/yyyy`
     
const today = new Date();
var date = today.getDate();
var month = today.getMonth() + 1;  //idx 0-jan, 1-fab..
var year = today.getFullYear();
if (date < 10) {
    date = '0' + date;
}
if (month < 10) {
    month = '0' + month;
}
console.log(`Todays Date ${month}-${date}-${year}`);
console.log(`Todays Date ${month}/${date}/${year}`);
console.log(`Todays Date ${date}-${month}-${year}`);
console.log(`Todays Date ${date}/${month}/${year}`);



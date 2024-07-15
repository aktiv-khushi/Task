//Arrays in JS.
/* Collection of items */
/*Arrays is mutable*/

//let marks = [97, 66, 55, 78, 84]
//console.log(marks)

//let marks = [97, 66, 55, 78, 84]
//let arrays = marks[0] = 79;
//console.log(marks)

//let cities = ["Junagadh","Rajkot","Ahmedabad","Mumbai","Pune"]
//
//for (let city of cities) {
//    console.log(city);
//}

//Example:

//let marks = [85,97,44,37,76,60];
//let sum = 0;
//
//for (let val of marks) {
//    sum = sum + val;
//}
//let avg = sum / marks.length;
//console.log("Avg marks = ",avg)

//let items = [250,645,300,900,50];
//let i = 0;
//for (let val of items) {
//    let offer = val / 10;
//    items[i] = items[i] - offer;
//    console.log(items[i])
//    i++;
//
//}

/*Arrays methods*/
/* push() add in item */
//let foodItems = ["potato","apple","litchi","tomato"]
//let add = foodItems.push("mango","burgur");
//console.log(add);

/* pop() delete from end in item */
//let foodItems = ["potato","apple","litchi","tomato"]
//let deleted = foodItems.pop();
//console.log(foodItems);

/* toString() convert arrays to string */
//let foodItems = ["potato","apple","litchi","tomato"];
//let marks = [97,86,54,36];
//console.log(foodItems);
//console.log(marks);
//console.log(foodItems.toString());
//console.log(marks.toString());

/* concat() joins multiple arrays & reruns result */
//let marvel_heroes = ["thor","spiderman","ironman"];
//let dc_heroes = ["superman","batman"]
//let indian_heroes = ["saktiman","krish"]
//let result = marvel_heroes.concat(dc_heroes, indian_heroes)
//console.log(result) // ['thor', 'spiderman', 'ironman', 'superman', 'batman','saktiman','krish']

/* unshift() add to start */
//let marvel_heroes = ["thor","spiderman","ironman"];
//let result = marvel_heroes.unshift("antman");
//console.log(result);

/* shift() delete to start */
//let marvel_heroes = ["thor","spiderman","ironman"];
//let result = marvel_heroes.shift();
//console.log(marvel_heroes);  //["spiderman","ironman"]

/* slice() return a piese of array */
//let marvel_heroes = ["thor","spiderman","ironman","antman"];
//console.log(marvel_heroes.slice(1)); // "spiderman"

/* splice() change original array(add,remove,replace) */
//let arr = [1,2,3,4,5,6,7];
//arr.splice(2,2,101,102)  //[1, 2, 101, 102, 5, 6, 7]
//arr.splice(2, 0, 101); //[1, 2, 101, 3, 4, 5, 6, 7]
//arr.splice(3 , 1)  //[1, 2, 3, 5, 6, 7] // 4 is delete.
//arr.splice(3 , 1 ,101); //[1, 2, 3, 101, 5, 6, 7]  //4 delete and add 101.

//Example:-
//let companies = ["bloomberg","microsoft","uber","google","IBM","Netflix"];
//let result = companies.shift();
//console.log("companies =",companies) //["microsoft","uber","google","IBM","Netflix"]
//console.log("result =",result)
//companies.splice(2, 1, "Ola")
//console.log(companies) //['bloomberg', 'microsoft', 'Ola', 'google', 'IBM', 'Netflix']
//companies.push("Amazon")
//console.log(companies)



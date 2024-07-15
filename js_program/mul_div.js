//5 .Image Operations: Write a JavaScript program to multiply and divide an image.

//Note : first of all index.html designing and onclick() code open further this code run.

function multiply() {
    n1 = document.getElementById("firstnumber").value;
    n2 = document.getElementById("secoundnumber").value;
    document.getElementById("result").innerHTML = n1 * n2
}
function divide() {
    n1 = document.getElementById("firstnumber").value;
    n2 = document.getElementById("secoundnumber").value;
    document.getElementById("result").innerHTML = n1 / n2
}

function substraction() {
    n1 = document.getElementById("firstnumber").value;
    n2 = document.getElementById("secoundnumber").value;
    document.getElementById("result").innerHTML = n1 - n2
}

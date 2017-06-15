var HOUR = 7;
var MINUTE = 15;
var PERIOD = "PM";

var string1, string2
if (MINUTE <= 30) {
    string1 = " just after ";
} else {
    string1 = " almost ";
    HOUR ++;
}
if (PERIOD === "AM") {
    string2 = " in the morning.";
} else {
    string2 = " in the evening."; 
}
console.log("It's"+ string1+ HOUR+ string2);
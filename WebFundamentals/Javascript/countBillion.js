
var count = 0;
var sum = 0;
var current = 0.01;
var count2 = 0;
var sum2 = 0;
var count3 = 0
var current2 = 0.01;
var sum3 = 0;
var current3 = 0.01;
var count4 = 0;

for (var i = 0; i < 30; i++) {
    count ++;
    sum += current;
    current *= 2;
    if (sum > 10000){
        count2++;
    }
}

while (sum2 < 1000000000) {
    sum2 += current2;
    current2 *= 2;
    count3 ++;
}

while (sum3 < Infinity) {
    sum3 += current3;
    current3 *= 2;
    count4 ++;
}

var count2 = count - count2;
console.log("He earned $" + sum);
console.log("It took him " + count2 + " days to reach $10,000.");
console.log("It took him " + count3 + " days to reach $1,000,000,000.");
console.log("It took him " + count4 + " days to reach Infinity!");
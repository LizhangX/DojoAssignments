
function printRange(Num1, Num2, Num3) {
    if(Num2 == null && Num3 == null){
        for (var i = 0; i < Num1; i++) {
            console.log(i);
        }
    } else if(Num3 == null && Num2 != null){
        for (var i = Num1; i < Num2; i++) {
            console.log(i);
        }
    } else {
        for (var i = Num1; i < Num2; i += Num3) {
            console.log(i);
        }
    }
}

printRange(-8,10,2);
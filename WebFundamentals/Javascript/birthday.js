var daysUntilMyBirthday = 60;

while(daysUntilMyBirthday > 0){
    if (daysUntilMyBirthday >30){
        console.log(daysUntilMyBirthday + " days until my birthday. Such a long time... :(");
        daysUntilMyBirthday --;
    } else if (daysUntilMyBirthday > 5) {
        console.log(daysUntilMyBirthday + " days until my birthday. Getting closer!");
        daysUntilMyBirthday --;
    } else if (daysUntilMyBirthday > 1) {
        console.log(daysUntilMyBirthday + " DAYS UNTIL MY BIRTHDAY!!!");
        daysUntilMyBirthday --;
    } else if (daysUntilMyBirthday === 1){
        console.log("♪ღ♪*•.¸¸¸.•*\¨\¨*•.¸¸¸.•*•♪ღ♪¸.•*\¨\¨*•.¸¸¸.•*•♪ღ♪•*")
        console.log("♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪")
        console.log("*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«")
        break
    }
}
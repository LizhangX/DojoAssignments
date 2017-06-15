
function randomChance(quarters, Num) {
    while (quarters > 0) {
        if(Math.floor(Math.random()*100) === 1){
            quarters = Math.floor(Math.random()*50) + 50 + quarters
            if (quarters >= Num) {
                return quarters;
            }
        }
        quarters--;
        if (quarters === 0){
            return 0;
        } 
    }
}
console.log(randomChance(100,100));
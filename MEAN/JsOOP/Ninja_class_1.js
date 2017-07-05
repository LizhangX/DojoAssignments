function Ninja(name) {
    this.name = name;
    this.health = 100;
    this.speed = 3;
    this.strength = 3;
}

Ninja.prototype.sayName = function(){
    console.log(`My ninja name is ${this.name}!`);
}
Ninja.prototype.showStats = function(){
    let show = `Name: ${this.name}, Health: ${this.health}, Speed: ${this.speed}, Strength: ${this.strength}`;
    console.log(show);
}
Ninja.prototype.drinkSake = function(){
    this.health += 10;
}

var ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
// -> "My ninja name is Hayabusa!"

ninja1.showStats();
// -> "Name: Hayabusa, Health: 100, Speed: 3, Strength: 3"
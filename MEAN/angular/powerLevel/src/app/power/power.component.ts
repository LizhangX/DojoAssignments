import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-power',
  templateUrl: './power.component.html',
  styleUrls: ['./power.component.css']
})
export class PowerComponent implements OnInit {
  level: number = 0;
  mylevel: number = 0;
  dropdown: number[] = [];

  


  constructor() {
    console.log("inside power");
    for (var i:number = 1; i < 101; i++) {
    this.dropdown.push(i);
    };
    console.log(this.dropdown);
  }

  ngOnInit() {

  }

  setLevel(level){
    console.log(level);
    this.mylevel= level;
    console.log(this.mylevel);
    
    
  }

}

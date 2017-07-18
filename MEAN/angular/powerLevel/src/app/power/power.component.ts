import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-power',
  templateUrl: './power.component.html',
  styleUrls: ['./power.component.css']
})
export class PowerComponent implements OnInit {
  level: number;
  mylevel: number = 0;
  dropdown: number[] = [];

  


  constructor() {
    console.log("inside power");
    for (var i = 1; i < 101; i++) {
    this.dropdown.push(i);
    };
    console.log(this.dropdown);
  }

  ngOnInit() {

  }

  onSubmit(){
    console.log(this.level);
    this.mylevel= this.level;
    console.log(this.mylevel);
    
    
  }

}

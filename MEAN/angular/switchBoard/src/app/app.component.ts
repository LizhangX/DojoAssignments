import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title: string = 'Switchboard';
  boxes: boolean[] = [true,true,true,true,true,true,true,true,true,true]
  display: string[] = ["ON","ON","ON","ON","ON","ON","ON","ON","ON","ON"];

  switch(idx) {
    this.boxes[idx] = !this.boxes[idx];
    if (this.boxes[idx] === true) {
      this.display[idx] = "ON";
    } else {
      this.display[idx] = "OFF";
    }
    console.log(this.boxes);
    
  }
}

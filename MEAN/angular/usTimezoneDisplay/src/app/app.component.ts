import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'US Time Zone Display';
  buttons: string[] = ['PST', 'MST', 'CST', 'EST'];
  
  today: number = Date.now();
  offset: number = new Date().getTimezoneOffset();
  UTCtoday: number = this.today + this.offset * 1000 * 60;
  currentTime: any;
  selected: any;
  time: object = {
    PST: this.UTCtoday - 1000 * 60 * 420,
    MST: this.UTCtoday - 1000 * 60 * 360,
    CST: this.UTCtoday - 1000 * 60 * 300,
    EST: this.UTCtoday - 1000 * 60 * 240,
  }

  getTime(button, idx){
    this.currentTime = this.time[button];
    this.selected = button;
    
  }
}

import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Retro Barcode Generator';
  colors: string[] = ['Aqua', 'Blue', 'CadetBlue', 'CornflowerBlue', 'DarkBlue', 'DodgerBlue'];


  // getColor(): any{
  //   return this.colors[Math.floor(Math.random() * this.colors.length)];
  // }

  ngOnInit() {
    //Called after the constructor, initializing input properties, and the first call to ngOnChanges.
    //Add 'implements OnInit' to the class.

    //randomly generate a random number of hex codes and push to this.colors
    function shuffle(a): void{
      for (let i = a.length; i; i--) {
          let j = Math.floor(Math.random() * i);
          [a[i - 1], a[j]] = [a[j], a[i - 1]];
      };
    }

    shuffle(this.colors);
    
  }
  // console.log(color);
  
}

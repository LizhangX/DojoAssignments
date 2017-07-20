import { Component, OnInit } from '@angular/core';
import { APIService } from '../api.service';

@Component({
  selector: 'app-burbank',
  templateUrl: './burbank.component.html',
  styleUrls: ['./burbank.component.css']
})
export class BurbankComponent implements OnInit {
  city: string = "burbank";
  weather = {};
  fullImagePath: string;

  constructor(private _api: APIService) { 
    this.fullImagePath = 'assets/images/burbank.jpeg'
    
  }

  getWeather(){
    this._api.retrieveWeather(this.city)
    .then( output => {
      console.log(output);
      this.weather = output;
    } )
    .catch( err => {console.log('err', err)})
  }
  ngOnInit() {
    this.getWeather()
  }

}

import { Component, OnInit } from '@angular/core';
import { APIService } from '../api.service';

@Component({
  selector: 'app-washington',
  templateUrl: './washington.component.html',
  styleUrls: ['./washington.component.css']
})
export class WashingtonComponent implements OnInit {
city: string = "washingtondc";
  weather = {};
  constructor(private _api: APIService) { }

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

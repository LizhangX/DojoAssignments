import { Component, OnInit } from '@angular/core';
import { APIService } from '../api.service';

@Component({
  selector: 'app-san-jose',
  templateUrl: './san-jose.component.html',
  styleUrls: ['./san-jose.component.css']
})
export class SanJoseComponent implements OnInit {
city: string = "sanjose";
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

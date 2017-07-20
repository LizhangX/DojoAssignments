import { Component, OnInit } from '@angular/core';
import { APIService } from '../api.service';


@Component({
  selector: 'app-chicago',
  templateUrl: './chicago.component.html',
  styleUrls: ['./chicago.component.css']
})
export class ChicagoComponent implements OnInit {
city: string = "chicago";
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

import { Component, OnInit } from '@angular/core';
import { APIService } from '../api.service';

@Component({
  selector: 'app-seattle',
  templateUrl: './seattle.component.html',
  styleUrls: ['./seattle.component.css']
})
export class SeattleComponent implements OnInit {
city: string = "seattle";
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

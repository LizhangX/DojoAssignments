import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs';

@Injectable()
export class APIService {

  constructor(private _http: Http) { }

  retrieveWeather(city) {
    console.log('inside service');
    return this._http.get(`http://api.openweathermap.org/data/2.5/weather?q=${city}&APPID=6ad5a5f015da7905001dfc4f4a25064e`).map(data=>data.json()).toPromise()
  }
}

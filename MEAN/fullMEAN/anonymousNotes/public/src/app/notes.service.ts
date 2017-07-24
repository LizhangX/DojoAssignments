import { Injectable } from '@angular/core';
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class NotesService {

  constructor(private _http: Http) {}

  getNotes(){
    return this._http.get('/notes').map(data => data.json()).toPromise();
  }

  createNote(note){
    return this._http.post('/notes', note).map( data => data.json()).toPromise();
  }
}

import { Component } from '@angular/core';
import { APIService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'GitHUb Score';
  score: any;
  error: any;
  newUser = {};

  onSubmit(newUser) {
    return this._api.getUser(newUser.username)
    .then(output => {console.log(output)
      this.score=output.public_repos + output.followers;
    })
    .catch(err => { console.log(err)
      this.error=err;
    })
  }
  constructor(private _api: APIService){

  }
}

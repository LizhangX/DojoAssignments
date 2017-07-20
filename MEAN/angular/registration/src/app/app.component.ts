import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Registration';
  user = {
    fname: '',
    lname: '',
    email: '',
    password: '',
    password_cm: '',
    address: '',
    unit: '',
    city: '',
    state: '',
    feeling: ''
  };
  success: boolean = false;
  newUser = {};

  onSubmit(){
    console.log(this.user);
    Object.assign(this.newUser, this.user)
    // this.user;
    console.log(this.newUser);
    
    this.success = true;
    
  }
}

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

  onSubmit(){
    this.success = true;
    
  }
}

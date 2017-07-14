import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Dojo Mail';
  emails: object[] = [
    {
      email: 'Bill@gates.com',
      importance: true,
      subject: 'New Windows',
      content: 'Windows XI will launch in year 2100.'
    },
    {
      email: 'Ada@lovelace.com',
      importance: true,
      subject: 'Programming',
      content: 'Enchantress of Numbers'
    },
    {
      email: 'John@carmac.com',
      importance: false,
      subject: 'Updated Algo',
      content: 'New algorithm for shadow volumes.'
    },
    {
      email: 'Gabe@newel.com',
      importance: false,
      subject: 'HL3!',
      content: 'Just kidding...'
    },
  ]
}

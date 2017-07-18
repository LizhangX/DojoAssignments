import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  quotes: object[] = [];
  quote = {votes: 0};

  onSubmit(myForm) {
    this.quotes.push(this.quote);
    this.quote = {votes:0};
    console.log(this.quotes);
    // myForm.valid = true;
    
    return false;
  }

  voteUp(quote){
    quote.votes++
    console.log(quote);
  }

  voteDown(quote){
    quote.votes--;
    console.log(quote);
  }

  delete(quotes, idx) {
    quotes.splice(idx,1);
  }
}

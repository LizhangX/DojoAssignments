import { Component, OnInit } from '@angular/core';
import { NotesService } from "./notes.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'Anonymous Notes';
  notes: any[] = [];
  note = {};

  constructor(
    private _noteService: NotesService
  ) {
  }

  ngOnInit(){
    this.getNotes();    
  }

  onSubmit(){
    this.createNote();
    this.getNotes();    
  }

  getNotes(){
      this._noteService.getNotes()
      .then(notes =>{ 
        console.log(notes);
        this.notes = notes})
      .catch(err => console.log(err));
  }
  
  createNote(){
    this._noteService.createNote(this.note)
    .then(
      user => {
        if (user.errors) {
          console.log('Error: ', user.errors.note.message);
        }
      }
    )
    this.note = {};
  }
}

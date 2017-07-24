import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from "@angular/forms";
import { HttpModule } from "@angular/http";

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SortByPipe } from './sort-by.pipe';

import { NotesService } from "./notes.service";

@NgModule({
  declarations: [
    AppComponent,
    SortByPipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpModule,
  ],
  providers: [NotesService],
  bootstrap: [AppComponent]
})
export class AppModule { }

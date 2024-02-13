import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import {LoginComponent} from "./login/login.component";
import {ListItemsComponent} from "./list-items/list-items.component";
import {GeneratorComponent} from "./generator/generator.component";
import {ScanComponent} from "./scan/scan.component";

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule
  ],
  declarations: [

  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }

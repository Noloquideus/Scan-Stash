import { Component } from '@angular/core';
import {MenuComponent} from "../menu/menu.component";
import {FormsModule} from "@angular/forms";
import {NgForOf} from "@angular/common";
import {MatCard} from "@angular/material/card";
import {MatFormField} from "@angular/material/form-field";
import {MatButton} from "@angular/material/button";
import {MatInput} from "@angular/material/input";

@Component({
  selector: 'app-list-items',
  standalone: true,
  imports: [MenuComponent, FormsModule, NgForOf, MatCard, MatFormField, MatButton, MatInput],
  templateUrl: './list-items.component.html',
  styleUrl: './list-items.component.css'
})

export class ListItemsComponent {
  keyword: string = '';
  allResults: string[] = ['place1-item1', 'place1-item2', 'place2-item1', 'place2-item2'];
  searchResults: string[] = [];

  onSearch() {
    // Логика поиска
    // Например, фильтрация по введенному ключевому слову
    this.searchResults = this.allResults.filter(result => result.includes(this.keyword));
  }
}

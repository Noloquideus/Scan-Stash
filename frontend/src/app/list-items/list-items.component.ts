import {Component} from '@angular/core';
import {MenuComponent} from "../menu/menu.component";
import {FormsModule} from "@angular/forms";
import {NgForOf} from "@angular/common";
import {MatCard} from "@angular/material/card";
import {MatFormField} from "@angular/material/form-field";
import {MatButton} from "@angular/material/button";
import {MatInput} from "@angular/material/input";
import {UserService} from "../services/user.service";
import {enviroment} from "../../enviroment/enviroment";

@Component({
  selector: 'app-list-items',
  standalone: true,
  imports: [MenuComponent, FormsModule, NgForOf, MatCard, MatFormField, MatButton, MatInput],
  templateUrl: './list-items.component.html',
  styleUrl: './list-items.component.css'
})

export class ListItemsComponent {

  constructor(private userService: UserService) {
  }
  keyword: string = '';
  allResults: string[] = ['place1-item1', 'place1-item2', 'place2-item1', 'place2-item2'];
  searchResults: string[] = [];

  onSearch() {
    // Логика поиска
    // Например, фильтрация по введенному ключевому слову
    if (enviroment.production) {
      this.userService.getAll().subscribe({
        next: result => {
          // filter result
        },
        error: e => alert("Error on search"),
      })
    } else {
      this.searchResults = this.allResults.filter(result => result.includes(this.keyword));
    }
  }
}

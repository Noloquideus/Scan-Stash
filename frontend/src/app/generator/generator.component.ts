import { Component } from '@angular/core';
import {MenuComponent} from "../menu/menu.component";
import {MatGridListModule} from "@angular/material/grid-list";
import {MatButtonModule} from '@angular/material/button';
import {NgForOf} from "@angular/common";
import {QRCodeModule} from "angularx-qrcode";
import {MatFormField} from "@angular/material/form-field";
import {FormsModule} from "@angular/forms";
import {MatInput} from "@angular/material/input";

@Component({
  selector: 'app-generator',
  standalone: true,
  imports: [MenuComponent, MatGridListModule, MatButtonModule, NgForOf, QRCodeModule, MatFormField, FormsModule, MatInput],
  templateUrl: './generator.component.html',
  styleUrl: './generator.component.css'
})
export class GeneratorComponent {
  places: string[] = [];
  items: string[] = [];
  numberOfPlaces: number = 0;
  numberOfItems: number = 0;

  generateQRCodes(): void {
    this.places = this.generateQRData('place', this.numberOfPlaces);
    this.items = this.generateQRData('item', this.numberOfItems);
  }

  private generateQRData(prefix: string, count: number): string[] {
    const qrData: string[] = [];
    let id = Math.floor(Date.now() / 100);

    for (let i = 0; i < count; i++) {
      qrData.push(`${prefix}:${id}`);
      id++;
    }

    return qrData;
  }

  print() {
    window.print();
  }
}

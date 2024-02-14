import { Component } from '@angular/core';
import {MenuComponent} from "../menu/menu.component";

@Component({
  selector: 'app-scan',
  standalone: true,
  imports: [MenuComponent],
  templateUrl: './scan.component.html',
  styleUrl: './scan.component.css'
})
export class ScanComponent {

}

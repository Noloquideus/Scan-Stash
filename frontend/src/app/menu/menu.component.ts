import {ChangeDetectorRef, Component} from '@angular/core';
import {MatButtonToggleModule} from '@angular/material/button-toggle';
import {Router} from "@angular/router";
import {scan} from "rxjs";

@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [MatButtonToggleModule],
  templateUrl: './menu.component.html',
  styleUrl: './menu.component.css'
})
export class MenuComponent {
  page: string = "scan";

  constructor(
    private router: Router,
    private cd: ChangeDetectorRef
  ) {
  }

  ngOnInit(): void {
    // Check if user is logged in
    console.log(this.router.url, this.router.routerState);
    const cleanUrl = this.router.url.substring(1);

    if (cleanUrl) {
      this.page = cleanUrl;
      this.cd.markForCheck();
      console.log('this.page', this.page);
    }
  }


  action(act: string) {
    console.log(act, this.page);
    this.router.navigate(['/'+act]);
  }
}

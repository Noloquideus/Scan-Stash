import {Component, OnDestroy, OnInit} from '@angular/core';
import {Router} from '@angular/router';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {ErrorStateMatcher} from '@angular/material/core';
import {MatButtonModule} from '@angular/material/button';
import {FormControl, FormGroupDirective, FormsModule, NgForm, ReactiveFormsModule, Validators,} from '@angular/forms';
import {AuthService} from "../services/auth.service";
import {enviroment} from "../../enviroment/enviroment";

export class MyErrorStateMatcher implements ErrorStateMatcher {
  isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
    const isSubmitted = form && form.submitted;
    return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
  }
}

@Component({
  selector: 'app-login',
  standalone: true,
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: [FormsModule, MatFormFieldModule, MatInputModule, ReactiveFormsModule, MatButtonModule]
})
export class LoginComponent implements OnInit {
  username: string | null = '';
  password: string | null = '';
  usernameFormControl = new FormControl('', [Validators.required]);
  passwordFormControl = new FormControl('', [Validators.required]);
  matcher = new MyErrorStateMatcher();

  constructor(private router: Router, private authService: AuthService) { }

  ngOnInit(): void {
    // Check if user is logged in
    if (localStorage.getItem('isLoggedIn') === 'true') {
      this.router.navigate(['/list-items']);
    }
  }

  login() {
    // Your login logic here
    // Assuming login is successful, set a flag in localStorage
    this.username = this.usernameFormControl.getRawValue();
    this.password = this.passwordFormControl.getRawValue();

    console.log(this.usernameFormControl.getRawValue(), this.passwordFormControl.getRawValue());

    if (enviroment.production) {
      this.authService.login(this.username, this.password).subscribe({
        next: data => {
          localStorage.setItem('isLoggedIn', 'true');
          this.router.navigate(['/list-items']);
        },
        error: err => {
          alert('Invalid username or password');
        }
      });
    } else {
      if (this.username === 'username' && this.password === 'password') {
        // Set isLoggedIn flag to true in local storage
        localStorage.setItem('isLoggedIn', 'true');
        // Redirect the user to list-items component
        this.router.navigate(['/list-items']);
      } else {
        alert('Invalid username or password');
      }
    }
  }
}

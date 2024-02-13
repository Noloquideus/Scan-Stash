import { CanActivateFn } from '@angular/router';

export const authGuard: CanActivateFn = (route, state) => {
  if (localStorage.getItem('isLoggedIn') === 'true') {
    return true; // Allow access
  } else {
    // Redirect to login page if not logged in
    //this.router.navigate(['/login']);
    return false;
  }
};

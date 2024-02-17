import {CanActivateFn, Router} from '@angular/router';
import {inject} from "@angular/core";

export const authGuard: CanActivateFn = (route, state) => {
  const router = inject(Router);
  if (localStorage.getItem('isLoggedIn') === 'true') {
    return true; // Allow access
  } else {
    // Redirect to login page if not logged in
    router.navigate(['/login']);
    return false;
  }
};

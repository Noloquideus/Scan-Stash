import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";


const headers = new HttpHeaders({'Content-Type' : 'application/json'});


const AUTH_URL = "http://localhost:8000/auth/login";

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  login(username: string | null, password: string | null) {
    return this.http.post(AUTH_URL, { username, password }, {headers: headers, withCredentials: true});
  }
}

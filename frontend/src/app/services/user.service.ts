import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {AddProduct} from "../models/add-product";
import {Place} from "../models/place";
import {ProductInfo} from "../models/product-info";
import {Observable} from "rxjs";
import {SearchResults} from "../models/search-results";

const API_URL = "http://localhost:8000/";

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  addProduct(addProduct: AddProduct) {
    return this.http.put(API_URL + "product/add", addProduct, { withCredentials: true });
  }

  addPlace(addPlace: Place) {
    return this.http.put(API_URL + "place/add", addPlace, { withCredentials: true });
  }

  getPlaceInfo(placeName: string) {
    return this.http.get(API_URL + "place/get_info/?place_name=" + placeName,{ withCredentials: true });
  }

  getProductInfo(productInfo: ProductInfo) {
    return this.http.get(API_URL + "product/get_info/?product_info=" +
      encodeURIComponent(JSON.stringify(productInfo)), { withCredentials: true });
  }

  getAll(): Observable<SearchResults | Object> {
    return this.http.get(API_URL + "search", { withCredentials: true });
  }
}

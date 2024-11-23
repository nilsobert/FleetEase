import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseURL = 'http://127.0.0.1:5000';
  constructor(private http: HttpClient) { }

  /*getJson(data: any): Observable<any> {
    return this.http.get(`${this.baseURL}/${data}`);
  }
*/
  /*sendJson(data: any): Observable<any> {
    return this.http.post(`${this.baseURL}/items/`, data);
  }
*/
  getJsonvehicle(): Observable<any> {
    return this.http.get(`${this.baseURL}/vehicles`);
  }

  getJsoncustomers(): Observable<any> {
    return this.http.get(`${this.baseURL}/customers`);
  }

  getJsonapplication(): Observable<any> {
    return this.http.get(`${this.baseURL}/applicationStatistics`);
  }


}

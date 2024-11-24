import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
}) // Automatically provides this service application-wide
export class ApiService {
  private apiUrl = 'http://159.65.113.122:5000/vehicles'; // Replace with your Python API endpoint

  constructor(private http: HttpClient) {}

  getData(): Observable<any> {
    return this.http.get(this.apiUrl);
  }
}

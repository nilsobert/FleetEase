import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
}) // Automatically provides this service application-wide
export class ApiService {
  private apiUrl = 'http://104.248.41.81:5000/system'; // Replace with your Python API endpoint

  constructor(private http: HttpClient) {}

  getData(): Observable<any> {
    return this.http.get(this.apiUrl);
  }
}

export class ApiServiceCarFleet {
  private apiUrl = 'http://104.248.41.81:5000/car_state'; // Replace with your Python API endpoint

  constructor(private http: HttpClient) {}

  getData(): Observable<any> {
    return this.http.get(this.apiUrl);
  }
}


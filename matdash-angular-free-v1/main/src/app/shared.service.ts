import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SharedService {
  // Using BehaviorSubject to share data
  private jsonDataSource = new BehaviorSubject<any>(null);
  jsonData$ = this.jsonDataSource.asObservable();

  // Method to update the value
  updateValue(data: any){
    this.jsonDataSource.next(data);
  }
}
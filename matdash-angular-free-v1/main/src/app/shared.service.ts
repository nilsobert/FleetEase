import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  private vehiclesSubject = new BehaviorSubject<any>(null);
  vehicles$ = this.vehiclesSubject.asObservable();

  setVehicles(vehicles: any) {
    this.vehiclesSubject.next(vehicles);
  }
}
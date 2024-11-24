import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  private systemSubject = new BehaviorSubject<any>(null);
  system$ = this.systemSubject.asObservable();

  setSystemsharefunction(systemshare: any) {
    this.systemSubject.next(systemshare);
  }
}

export class SharedServiceCar {
  private carSubject = new BehaviorSubject<any>(null);
  car$ = this.carSubject.asObservable();

  setCarsharefunction(carshare: any) {
    this.carSubject.next(carshare);
  }
}
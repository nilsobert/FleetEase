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
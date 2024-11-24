import { Component, OnDestroy } from '@angular/core';
import { MaterialModule } from '../../material.module';
import { MatMenuModule } from '@angular/material/menu';
import { MatButtonModule } from '@angular/material/button';
import { CommonModule } from '@angular/common';
import { SharedServiceCar } from '../../shared.service';
import { record, array, number, decodeType, decode } from 'typescript-json-decoder';
import { RouterOutlet } from '@angular/router';
import { Subscription, interval } from 'rxjs';
import { ApiServiceCarFleet } from '../../api.service';
import { OnInit } from '@angular/core';

export interface productsData {
  id: number;
  imagePath: string;
  uname: string;
  position: string;
  hrate: number;
  skills: string;
  priority: string;
  progress: string;
}

const ELEMENT_DATA: productsData[] = [
  {
    id: 1,
    imagePath: 'assets/images/products/dash-prd-1.jpg',
    uname: 'Dusty Rusty',
    position: 'Car ID 74',
    skills: '0',
    hrate: 35.2,
    priority: 'On the Way',
    progress: 'warning',
  },
  {
    id: 2,
    imagePath: 'assets/images/products/dash-prd-2.jpg',
    uname: 'Wheely McWheel',
    position: 'Car ID 7',
    skills: '4',
    hrate: 73.8,
    priority: 'In Usage',
    progress: 'success',
  },
  {
    id: 3,
    imagePath: 'assets/images/products/dash-prd-3.jpg',
    uname: 'Sir Honksalot',
    position: 'Car ID 13',
    skills: '0',
    hrate: 51.8,
    priority: 'Idle',
    progress: 'primary',
  },
  {
    id: 4,
    imagePath: 'assets/images/products/dash-prd-4.jpg',
    uname: 'Bumper Bumpface',
    position: 'Car ID 34',
    skills: '3',
    hrate: 94.0,
    priority: 'in Usage',
    progress: 'success',
  },
];
@Component({
  selector: 'app-revenue-product',
  standalone: true,
  imports: [MaterialModule, MatMenuModule, MatButtonModule, CommonModule],
  templateUrl: './revenue-product.component.html',
})
export class AppRevenueProductComponent //implements OnInit, OnDestroy 
{
  displayedColumns: string[] = ['assigned', 'progress', 'priority', 'budget'];
  dataSource = ELEMENT_DATA;
  /* private subscriptionCar: Subscription = new Subscription();
  public carsettings: any; */
  constructor(
   // private apiServiceCar: ApiServiceCarFleet,
    //private sharedServiceCar: SharedServiceCar,
  ) {}
   ngOnInit(): void {
    /* this.subscriptionCar.add(
      interval(1000).subscribe(() => {
        this.apiServiceCar.getData().subscribe({
          next: (response) => {
            console.log('API Response:', response);
            this.carsettings = response;
            this.sharedServiceCar.setCarsharefunction(this.carsettings);
          },
          error: (err) => {
            console.error('Error fetching data:', err);
          },
        });
      })
    ); */
  }

  ngOnDestroy(): void {
   /*  if (this.subscriptionCar) {
      this.subscriptionCar.unsubscribe();
    } */
  } 
 
}
 
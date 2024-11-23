import { Component, InjectionToken, NgModule, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
//import { ApiService } from './api.service';
import { FormsModule, NgModel } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Injectable } from '@angular/core';
import { DataService } from './api.service';



 @Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,HttpClientModule, //FormsModule, 
  CommonModule],

    /*template: `
  <div>
      <h1>Get JSON to API</h1>
      <form (submit)="sendJson()">
        <label>
          CPU:
          <input type="text" [(ngModel)]="jsonData.cpu_Usage" name="CPU" required />
        </label>
        <label>
          Price:
          <input
            type="number"
            [(ngModel)]="jsonData.ramn_Usage"
            name="RAM"
            required
          />
        </label>
        <button type="getJson()">Send JSON</button>
      </form>
      <pre>{{ response | json }}</pre>
 </div>`,  */
 template: `
    <div *ngIf="data">
      <h1>Real-Time Data</h1>
      <pre>{{ data | json }}</pre>
    </div>
  `,

  styles: [],
  templateUrl: './app.component.html', 
  styleUrl: './app.component.scss'
 
 })

export class AppComponent implements OnInit{
  title = 'FleetEase_Frontend';
  vehicles: any;
  customers: any;
  applicationStatics: any;
  data: any;
  
  
  constructor (//private apiService: ApiService, 
  private dataService: Dataservice){}
 // jsonData = {cpu_Usage: '', ramn_Usage: ''};
  


  //constructor(private dataService: DataService) {}



ngOnInit(){
 // this.getJsonvehicle();
  //this.getJsonapplcation();
  //this.getJsoncustomers();
  this.dataService.getDataStream().subscribe((response) => {
    this.data = response;
  })
}

/*
  getJsonvehicle(){
this.apiService.getJsonvehicle().subscribe((data)=>{this.vehicles = data;});
  }

  getJsoncustomers(){
    this.apiService.getJsoncustomers().subscribe((data)=>{this.customers = data;});
  }

  getJsonapplcation(){
    this.apiService.getJsonapplication().subscribe((data)=>{this.applicationStatics = data;});
  }


*/
}


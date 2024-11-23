import { Component, NgModule, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { ApiService } from './api.service';
import { FormsModule, NgModel } from '@angular/forms';




 @Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,HttpClientModule, FormsModule],

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
  templateUrl: './app.component.html', 
  styleUrl: './app.component.scss'
 })

export class AppComponent {
  title = 'FleetEase_Frontend';
  vehicles: any;
  customers: any;
  applicationStatics: any;
  constructor (private apiService: ApiService){}
 // jsonData = {cpu_Usage: '', ramn_Usage: ''};
  
ngOnInit(){
  this.getJsonvehicle();
  //this.getJsonapplcation();
  this.getJsoncustomers();
}

  getJsonvehicle(){
this.apiService.getJsonvehicle().subscribe((data)=>{this.vehicles = data;});
  }

  getJsoncustomers(){
    this.apiService.getJsoncustomers().subscribe((data)=>{this.customers = data;});
  }

  getJsonapplcation(){
    this.apiService.getJsonapplication().subscribe((data)=>{this.applicationStatics = data;});
  }

}




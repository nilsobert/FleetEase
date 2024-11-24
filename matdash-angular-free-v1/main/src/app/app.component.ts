import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ApiService } from './api.service';
import { Subscription, interval } from 'rxjs';
import { SharedService } from './shared.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
/*   template: `
  <div>
    <h1>Angular 19 Standalone Example</h1>
    <div *ngIf="data; else loading">
      <p>{{ data?.message }}</p>
    </div>
    <ng-template #loading>
      <p>Loading data...</p>
    </ng-template>
  </div>
`, */
  templateUrl: './app.component.html',
})
export class AppComponent implements OnInit{
  title = 'Modernize Angular Admin Tempplate';
  
  public vehicles: any;
  subscription: Subscription;
  constructor(private apiService: ApiService) {}



  ngOnInit(): void {
    this.subscription = interval(1000).subscribe(() => {
      this.apiService.getData().subscribe({
        next: (response) => {
          console.log('API Response:', response);
          this.vehicles = response;
        },
        error: (err) => {
          console.error('Error fetching data:', err);
      },
    });
  });
  }}

 

  


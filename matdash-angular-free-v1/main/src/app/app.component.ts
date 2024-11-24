import { Component, OnInit, OnDestroy } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ApiService } from './api.service';
import { Subscription, interval } from 'rxjs';
import { SharedService } from './shared.service';
import { ApiServiceCarFleet } from './api.service';
import { SharedServiceCar} from './shared.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'Modernize Angular Admin Template';
  
  public systemsettings: any;
  private subscription: Subscription = new Subscription();
  private subscriptionCar: Subscription = new Subscription();
  public carsettings: any;

  constructor(
    private apiService: ApiService,
    private sharedService: SharedService,
   // private apiServiceCar: ApiServiceCarFleet,
   // private sharedServiceCar: SharedServiceCar,
  ) {}

  ngOnInit(): void {
    this.subscription.add(
      interval(1000).subscribe(() => {
        this.apiService.getData().subscribe({
          next: (response) => {
            console.log('API Response:', response);
            this.systemsettings = response;
            this.sharedService.setSystemsharefunction(this.systemsettings);
          },
          error: (err) => {
            console.error('Error fetching data:', err);
          },
        });
      })
    );
  }

/*   ngOnInitCar(): void {
    this.subscriptionCar.add(
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
    );
  }

  ngOnDestroyCar(): void {
    if (this.subscriptionCar) {
      this.subscription.unsubscribe();
    }
  } */

  ngOnDestroy(): void {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
}
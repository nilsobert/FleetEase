import { Component, OnInit, OnDestroy } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ApiService } from './api.service';
import { Subscription, interval } from 'rxjs';
import { SharedService } from './shared.service';

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

  constructor(
    private apiService: ApiService,
    private sharedService: SharedService
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

  ngOnDestroy(): void {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
}
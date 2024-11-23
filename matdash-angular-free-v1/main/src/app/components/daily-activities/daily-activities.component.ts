import { Component } from '@angular/core';
import { MaterialModule } from '../../material.module';

interface stats {
  id: number;
  time: string;
  color: string;
  title?: string;
  subtext?: string;
  link?: string;
}

@Component({
  selector: 'app-daily-activities',
  standalone: true,
  imports: [MaterialModule],
  templateUrl: './daily-activities.component.html',
})
export class AppDailyActivitiesComponent {
  stats: stats[] = [
    {
      id: 1,
      time: '09.30 am',
      color: 'warning',
      title: 'Car ID 13 Damage reported',
    },
    {
      id: 2,
      time: '10.30 am',
      color: 'accent',
      subtext: '78 Users driven since 12 am',
      
    },
    {
      id: 3,
      time: '12.30 pm',
      color: 'warning',
      subtext: 'Premium User unhappy',
    },
    {
      id: 4,
      time: '13.00 pm',
      color: 'primary',
      title: 'New sale recorded',
      link: '#ML-3467',
    },
    {
      id: 5,
      time: '14.30 pm',
      color: 'error',
      subtext: 'Cyber Attack',
    },
    {
      id: 6,
      time: '15.30 pm',
      color: 'primary',
      subtext: 'FleetEase won the Hackatum',
    },
  ];
}

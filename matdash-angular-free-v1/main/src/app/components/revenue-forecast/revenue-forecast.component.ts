import { Component, OnInit, OnDestroy, ViewChild } from '@angular/core';
import { MaterialModule } from '../../material.module';
import { TablerIconsModule } from 'angular-tabler-icons';
import {
  ApexChart,
  ChartComponent,
  ApexDataLabels,
  ApexLegend,
  ApexStroke,
  ApexTooltip,
  ApexAxisChartSeries,
  ApexPlotOptions,
  NgApexchartsModule,
  ApexFill,
} from 'ng-apexcharts';
import { AppComponent } from 'src/app/app.component';
import { FormsModule } from '@angular/forms';
import { Subscription } from 'rxjs';
import { SharedService } from '../../shared.service';

export interface RevenueForecastChart {
  series: ApexAxisChartSeries;
  chart: ApexChart;
  dataLabels: ApexDataLabels;
  plotOptions: ApexPlotOptions;
  tooltip: ApexTooltip;
  stroke: ApexStroke;
  legend: ApexLegend;
  fill: ApexFill;
}

interface Month {
  value: string;
  viewValue: string;
}

@Component({
  selector: 'app-revenue-forecast',
  standalone: true,
  imports: [MaterialModule, TablerIconsModule, NgApexchartsModule, FormsModule],
  templateUrl: './revenue-forecast.component.html',
})
export class AppRevenueForecastComponent implements OnInit , OnDestroy{
  @ViewChild('chart') chart: ChartComponent = Object.create(null);
  public revenueForecastChart!: Partial<RevenueForecastChart> | any;

 
  onMonthChange() {
    this.updateChartData();
    this.initChart();
  }

  months: Month[] = [
    { value: 'CPU', viewValue: 'CPU Outage' },
    { value: 'RAM', viewValue: 'RAM Outage' },
  ];

  selectedMonth: string = 'CPU';
  systemdata: any;
  valueCPU1: number[] = [];
  valueCPU2: number[] = [];
  private subscription: Subscription = new Subscription();
  constructor(private sharedService: SharedService) {
    this.updateChartData();
    this.initChart();
  }

  ngOnInit() {
    this.subscription.add(
      this.sharedService.system$.subscribe((systemsshare) => {
        this.systemdata = systemsshare;
      })
    );
  }


  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
  updateChartData() {
    if (this.selectedMonth === 'CPU') {
      this.valueCPU1 = [30, 40, 25, 43, 51, 37];
      this.valueCPU2 = [20, 26, 13, 32, 40, 20];
    } else {
      this.valueCPU1 = [40, 50, 35, 53, 61, 47];
      this.valueCPU2 = [30, 36, 23, 42, 50, 30];
    }
  }

  initChart() {
    this.revenueForecastChart = {
      series: [
        {
          name: 'Random Algorithm',
          data: this.valueCPU1,
        },
        {
          name: 'FleetEase Algorithm',
          data: this.valueCPU2,
        },
      ],
      chart: {
        type: 'line',
        fontFamily: 'inherit',
        foreColor: '#adb0bb',
        height: 300,
        stacked: true,
        offsetX: -15,
        toolbar: {
          show: false,
        },
      },
      colors: ['rgba(99, 91, 255, 1)', 'rgba(255, 102, 146,1)'],
      plotOptions: {
        bar: {
          horizontal: false,
          barHeight: '60%',
          columnWidth: '15%',
          borderRadius: [6],
          borderRadiusApplication: 'end',
          borderRadiusWhenStacked: 'all',
        },
      },
      dataLabels: {
        enabled: false,
      },
      legend: {
        show: false,
      },
      grid: {
        show: true,
        padding: {
          top: 0,
          bottom: 0,
          right: 0,
        },
        borderColor: 'rgba(0,0,0,0.05)',
        xaxis: {
          lines: {
            show: true,
          },
        },
        yaxis: {
          lines: {
            show: true,
          },
        },
      },
      yaxis: {
        min: 0,
        max: 100,
        tickAmount: 4,
      },
      xaxis: {
        axisBorder: {
          show: false,
        },
        axisTicks: {
          show: false,
        },
        categories: [
          '1ms',
          '5ms',
          '10ms',
          '15ms',
          '20ms',
          '25ms',
        ],
        labels: {
          style: { fontSize: '13px', colors: '#adb0bb', fontWeight: '400' },
        },
      },
      tooltip: {
        theme: 'dark',
        x: {
          show: false,
        },
      },
    };
  }
}


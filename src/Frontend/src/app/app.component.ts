import { Component, OnInit } from '@angular/core';
import { StreamService } from './oboe.service';

@Component({
  selector: 'app-stream',
  template: `
    <div *ngIf="error" class="error">Error: {{ error }}</div>
    <div *ngIf="data">
      <h1>Value: {{ data.value }}</h1>
      <p>Timestamp: {{ data.timestamp }}</p>
    </div>
  `,
  styles: ['.error { color: red; }']
})
export class StreamComponent implements OnInit {
  data: any = null;
  error: string | null = null;

  constructor(private streamService: StreamService) {}

  ngOnInit(): void {
    this.streamService.connectToStream(
      'http://172.0.0.1:5000/test_streaming',
      (data) => (this.data = data), // Update data on each JSON object
      (err) => (this.error = `Stream error: ${err.message || err}`)
    );
  }
}
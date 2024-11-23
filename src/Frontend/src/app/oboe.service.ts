import { Injectable } from '@angular/core';
import * as oboe from 'oboe';

@Injectable({
  providedIn: 'root'
})
export class StreamService {
  connectToStream(url: string, callback: (data: any) => void, errorCallback: (err: any) => void): void {
    oboe(url)
      .node('!', (data: any) => {
        callback(data); // Process each streamed JSON object
        return oboe.drop; // Prevent memory buildup by discarding already processed data
      })
      .fail((error: any) => {
        errorCallback(error);
      });
  }
}

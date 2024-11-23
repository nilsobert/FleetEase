import { TestBed } from '@angular/core/testing';

import { OboeService } from './oboe.service';

describe('OboeService', () => {
  let service: OboeService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(OboeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

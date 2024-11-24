import { TestBed } from '@angular/core/testing';
import { ApiServiceCarFleet } from './api.service';
import { ApiService } from './api.service';

describe('ApiService', () => {
  let service: ApiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

describe('ApiServiceCar', () => {
  let Car: ApiServiceCarFleet;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    Car = TestBed.inject(ApiServiceCarFleet);
  });

  it('should be created', () => {
    expect(Car).toBeTruthy();
  });
});

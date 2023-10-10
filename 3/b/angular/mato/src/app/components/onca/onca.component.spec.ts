import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OncaComponent } from './onca.component';

describe('OncaComponent', () => {
  let component: OncaComponent;
  let fixture: ComponentFixture<OncaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [OncaComponent]
    });
    fixture = TestBed.createComponent(OncaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

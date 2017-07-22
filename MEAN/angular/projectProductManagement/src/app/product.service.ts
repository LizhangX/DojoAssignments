import { Injectable } from '@angular/core';
import { BehaviorSubject } from "rxjs/BehaviorSubject";

@Injectable()
export class ProductService {

  constructor() { }
  observedProducts = new BehaviorSubject(null);

  updateProduct(Products: object) {
    this.observedProducts.next(Products);
  }
}

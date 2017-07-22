import { Component, OnInit, OnDestroy } from '@angular/core';
import { ProductService } from "../product.service";
import { Subscription } from "rxjs/Subscription";

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})

export class ProductsComponent implements OnInit, OnDestroy {
  subscription: Subscription;
  products = [];

  constructor(private _productService: ProductService) { 
    // _productService.observedProducts.getValue()

    this.subscription = _productService.observedProducts.subscribe(
      (updatedUsers) => { this.products = updatedUsers; },
    )
  }

  ngOnInit() {
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

}
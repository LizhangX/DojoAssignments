import { Component, OnInit, OnDestroy } from '@angular/core';
import { ProductService } from "../product.service";
import { Subscription } from "rxjs/Subscription";
import { Router } from "@angular/router";

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})
export class CreateComponent implements OnInit, OnDestroy {
  subscription: Subscription;
  products = [];
  newProduct = {};

  constructor(
    private _productService: ProductService,
    private _router: Router
  ) { 
    // _productService.observedProducts.getValue()
    this.subscription = _productService.observedProducts.subscribe(
      (updatedUsers) => { this.products = updatedUsers; },
    )
  }

  creatProduct(){
    this.products.push(this.newProduct);
    this._productService.updateProduct(this.products);
    this.newProduct = {};    
  }

  ngOnInit() {
    this.newProduct = {};
  }

  onSubmit(){
    this.creatProduct();
    this._router.navigate(['/products'])

  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

}

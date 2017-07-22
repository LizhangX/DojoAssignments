import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router, ActivatedRoute } from "@angular/router";
import { ProductService } from "../product.service";
import { Subscription } from "rxjs/Subscription";

@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.css']
})
export class EditComponent implements OnInit, OnDestroy {

products: object[];
Product = {};
id: any;
subscription: Subscription;

  constructor(
    private _route: ActivatedRoute,
    private _router: Router,
    private _productService: ProductService
  ) {
    this._route.params.subscribe((param)=>{
      console.log(param.id);
      this.id = param.id;
      
    });
    
    this.subscription = this._productService.observedProducts.subscribe(
      (updatedProducts) => this.products=updatedProducts,
    )

  }

  ngOnInit() {
    this.Product = this.products[this.id];
  }

  onSubmit(){
    this.editProduct();
    this._router.navigate(['/products']);
  }


  delete(){
    this.products.splice(this.id,1);
    this._router.navigate(['/products'])
  }

  editProduct() {
    this.products[this.id] = this.Product;
    this._productService.updateProduct(this.products);
    this.Product = {};
  }

  ngOnDestroy(){
    this.subscription.unsubscribe();
  }
}

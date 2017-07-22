import { Component,OnDestroy } from '@angular/core';
import { BehaviorSubject } from "rxjs/BehaviorSubject";
import { ProductService } from "./product.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'PPM - Project Product Management';
  products: object[] = [
    {
      title: 'camera',
      price: '100',
      imgUrl: ''
    },
    {
      title: 'Macbook',
      price: '1000',
      imgUrl: ''
    },
  ];
  product = {};

  constructor(private _productService: ProductService){
    _productService.updateProduct(this.products);
    _productService.observedProducts.subscribe(
      (products) => { this.products = products; }
    );
  }

}

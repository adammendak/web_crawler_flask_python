import { Component } from '@angular/core';
import {HttpService} from '../service/http.service';
import {SingleElement} from "../model/SingleElement";

@Component({
  selector: 'app-form-template',
  templateUrl: './form-template.component.html',
  styleUrls: ['./form-template.component.css']
})
export class FormTemplateComponent {

  constructor(private httpService: HttpService) { }

  count: String = '';
  name: String = '';
  created_at: String = '';
  updated_at: String = '';
  listOfElements: Array<SingleElement> = [];

  addUrl(url) {
    this.httpService.addUrl(url).subscribe(response => {
      console.log(response);
      this.count = response.count;
      this.name = response.name;
      this.updated_at = response.updated_at;
      this.created_at = response.created_at;
      this.listOfElements = response.elements;
      console.log(this.listOfElements)
    });
  }

}



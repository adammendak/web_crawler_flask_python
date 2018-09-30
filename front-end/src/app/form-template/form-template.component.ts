import { Component, OnInit } from '@angular/core';
import {HttpService} from '../service/http.service';

@Component({
  selector: 'app-form-template',
  templateUrl: './form-template.component.html',
  styleUrls: ['./form-template.component.css']
})
export class FormTemplateComponent {
  constructor(private myhttpService: HttpService) {}

  addUrl(url) {
    console.log(url);

    this.myhttpService.addUrl(url).subscribe(response => {
      console.log(response);
    });
  }

  }

// const j: JSON = <JSON>({
//   domain: 'text domain',
//   paragrafy: 10,
//   text: 'lorem'
// });
// this.myhttpServise.addPost(j).subscribe(json => {
//   console.log(post);
// });


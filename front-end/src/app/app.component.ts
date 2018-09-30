import {Component, OnInit} from '@angular/core';
import {HttpService} from './service/http.service';
import {HttpClient} from '@angular/common/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [HttpService]

})
export class AppComponent  {
  // constructor (private httpservice: HttpService, private http: HttpClient) {
  // ngOnInit() {
  //   const obs = this.http.post('http://crawler.adammendak.pl/domain');
  //   obs.subscribe((response) => console.log(response));
  // }
}


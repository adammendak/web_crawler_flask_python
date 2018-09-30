import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';



@Injectable()
export class HttpService {
  URL: string= 'http://crawler.adammendak.pl/domain';

  constructor(private http: HttpClient) { }

  addUrl(url): Observable<any> {
    return this.http.post(this.URL, {'domain' : url});
  }
}

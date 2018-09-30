import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';



@Injectable()
export class HttpService {
  readonly URL: string= 'http://crawler.adammendak.pl/domain';
  // readonly param: HttpParams;

  constructor(private http: HttpClient, ) {

    }

  addUrl(url): Observable<any> {
    return this.http.post(this.URL, {'domain' : url});
  }


}

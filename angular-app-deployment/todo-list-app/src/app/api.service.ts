import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {environment} from "../environments/environment"
@Injectable({
  providedIn: 'root'
})
export class ApiService {
  BASE_URL = environment.BASE_URL
  constructor(private http:HttpClient) { }
  settodoData(data: any): any{
    return this.http.post(this.BASE_URL+'/api/item',data);
  }
  getTodoData(data : any):any
  {
    return this.http.post(this.BASE_URL+'/api/list',data)
  }
  deleteTodoData(data:any):any
  {
    return this.http.post(this.BASE_URL+"/api/delete",data)
  }
  updateData(data: any):any
  {
    return this.http.post(this.BASE_URL+'/api/update',data)
  }
}

import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DeleteComponent } from './delete/delete.component';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';
import { InsertComponent } from './insert/insert.component';
import { ListComponent } from './list/list.component';
import { LoginComponent } from './login/login.component';
import { UpdateComponent } from './update/update.component';
import { AngularFireAuthGuard } from '@angular/fire/compat/auth-guard'
import { SignupComponent } from './signup/signup.component';

const routes: Routes = [
    
      {
        path:"login",
        component:LoginComponent
      },
      {
        path:"",
        component:LoginComponent
      },
      {
        path:"signup",
        component:SignupComponent
      },
    {
    path :"",
    component: HeaderComponent,
    children:[
      {
        path:"home",
        component:HomeComponent,
        canActivate:[AngularFireAuthGuard]
      },
      {
          path : "insert",
          component:InsertComponent,
          canActivate :[AngularFireAuthGuard]
      },
      {
          path :"update",
          component: UpdateComponent,
          canActivate :[AngularFireAuthGuard]
      },
      {
        path:"list",
        component:ListComponent,
        canActivate :[AngularFireAuthGuard]
      },
      {
        path:"delete",
        component : DeleteComponent,
        canActivate :[AngularFireAuthGuard]
      },
     
    ],
  
  },
 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

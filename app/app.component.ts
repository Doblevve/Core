import { Component,OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { UserService } from './services/user.service';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
    title = 'frontend';
    users: any = [];

    constructor (private userService:UserService ){}

    ngOnInit(): void {
      this.userService.getUsuarios().subscribe(data =>{
        this.users = data;
      }) 
    }
}
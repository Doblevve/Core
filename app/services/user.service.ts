// Importa el decorador Injectable para que Angular sepa que esta clase puede ser inyectada como dependencia
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// El decorador @Injectable marca esta clase como un servicio que puede ser inyectado en otros componentes o servicios
@Injectable({
  // 'providedIn: root' hace que este servicio esté disponible de forma global en toda la aplicación (singleton)
  providedIn: 'root'
})
export class UserService {
  private apiUrl = 'http://localhost:8000'; // URL base de tu backend
  
  // Constructor de la clase. Aquí se pueden inyectar otros servicios, como HttpClient si quieres hacer llamadas a una API
  constructor(private http: HttpClient) { }
  
  getUsuarios(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/usuarios`);
  }

  // Aquí es donde agregarás los métodos que harán la lógica del servicio
  // Por ejemplo: obtener usuarios, registrar un usuario, etc.
}

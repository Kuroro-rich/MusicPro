/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/WebServices/WebService.java to edit this template
 */
package service;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

/**
 *
 * @author lonso
 */
@WebService(serviceName = "ServiceMusicpro")
public class ServiceMusicpro {

    /**
     * Web service operation
     */
    @WebMethod(operationName = "login")
    public boolean login(@WebParam(name = "user") String user, @WebParam(name = "pass") String pass) {
       if (user.equals("user1") && pass.equals("pass1")){
            return true;
        }else{
            return false;
        }
    }

    @WebMethod(operationName = "producto")
    public int producto(@WebParam(name = "categoria") String categoria, @WebParam(name = "precio") int precio) {
       if(categoria.equals("guitarra")){
            precio=50000;
            return precio;
        }
        if(categoria.equals("bajo")){
            precio=60000;
            return precio;
        }
        if(categoria.equals("teclado")){
            precio=100000;
            return precio;
        }
        if(categoria.equals("flauta")){
            precio=15000;
            return precio;
        }
        else{return 0;}
    }

    @WebMethod(operationName = "pago")
    public int pago(@WebParam(name = "total") int total, @WebParam(name = "pago") int pago) {
      if(pago >= total){
            return pago - total;
        }else{
            return -1;
        }
    }

    
    
}
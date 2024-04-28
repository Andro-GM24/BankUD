/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package cafeteria_decorator;

import adiciones.*;
import java.util.Scanner;
/**
 *
 * @author Estudiantes
 */
public class Cafeteria_Decorator {
    
    static Cafe b;
    
    public void darDatos(Cafe b){
        System.out.println("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////");
         System.out.println("su factura es de " + b.getPrecio() + " pesos y contiene "+ b.getDescripcion());
         System.out.println("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////");
    }
   

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        /*CafeBasico a = new CafeBasico();*/
        Cafeteria_Decorator cafeteria = new Cafeteria_Decorator();
       
        Scanner leer = new Scanner(System.in);
       char numero_opcion=0;
       System.out.println("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////");
       
        System.out.println("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////");
        System.out.println("/////////////////////////////////////////// BIENVENIDO//////////////////////////////////////////////////////////////////////////");
        System.out.println("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////");
        System.out.println("/////////////////////////////////ELIJA//SU//CAFE ESCRIBIENDO EL NUMERO DEL CAFE A PEDIR/////////////////////////////////////////");
        System.out.println("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////1.Mocca////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////2.irish////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////3.latte////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////4.Americano////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////5.Capuccino////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////6.Carajillo////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////7.Azteca////////////////////////////////////////////////////////////////////////");
        System.out.println("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////");
        
        do{
         numero_opcion=leer.next().charAt(0);
        
        
        switch(numero_opcion) {
            case '1' -> {
                 b = new Chocolate(new Leche(new EspumadeLeche(new CafeBasico())));
                break;
            }
            
            case '2' ->{
                b= new Wiskhy(new EspumadeLeche(new CafeBasico()));
                break;
            }
            
            case '3' ->{
                b= new Leche(new EspumadeLeche(new CafeBasico()));
                break;
            }
            case '4' ->{
                b=new Agua(new CafeBasico());
                break;
            }
            case '5' ->{
                b= new Leche(new EspumadeLeche(new CafeBasico()));
                break;
            }
            
            case '6' ->{
                b= new Brandy(new CafeBasico());
                break;
            }
            case '7' ->{
               /* b=new Leche(new Hielo(new Helado(new CafeBasico())));*/
               b = new Leche(b); 
                break;
            } 
            
        }
        /*tablero de adiciones*/
        System.out.println("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////");
        System.out.println("/////////////////////////////////ELIJA//SU//ADICIÓN ESCRIBIENDO EL NUMERO DEL ADICIÓN A PEDIR/////////////////////////////////////////");
        System.out.println("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////1.Agua////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////2.Brandy////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////3.Chocolate////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////4.Helado////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////5.Hielo////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////6.Leche////////////////////////////////////////////////////////////////////////");
        System.out.println("//////////////////////////////////////////7.whisky////////////////////////////////////////////////////////////////////////");
        System.out.println("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////");
        System.out.println("si quiere pedir otro ingrese 0 si no ingrese cualquier caracter ");
        /*do while de adiciones*/
        do{
            numero_opcion=leer.next().charAt(0);
            
            switch(numero_opcion) {
            case '1' -> {
                 b = new Agua(b); 
                break;
            }
            
            case '2' ->{
               b = new Brandy(b); 
                break;
            }
            
            case '3' ->{
                b = new Chocolate(b); 
                break;
            }
            case '4' ->{
                b = new Helado(b); 
                break;
            }
            case '5' ->{
                b = new Hielo(b); 
                break;
            }
            
            case '6' ->{
                b = new Leche(b); 
                break;
            }
            case '7' ->{
               
               b = new Wiskhy(b); 
                break;
            } 
            
        }
            
            
            
        }while(numero_opcion=='0');
        
        
        cafeteria.darDatos(b);
        
        b=null;
        
        
        
        
            System.out.println("si quiere pedir otro ingrese 0 si no ingrese cualquier caracter ");
            numero_opcion=leer.next().charAt(0);
        
            
           
             
        }while(numero_opcion=='0');
           
            
        
        
        
        
        
        
    
    }
    
}
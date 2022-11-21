
package memoria;

import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;


public class Juego {
    
    //atributos
    JFrame ventana;
    //presentacion 
    JPanel panelPresentacion;
    JLabel fondoPresentacion;
    JLabel BotonJugar;
    //juego
    JPanel panelJuego;
    JLabel matriz[][];
    int mat[][];
    int Aux
    String Jugador;
    Random aleatorio;
    
    //constructor
    public Juego(){
    
        //ventana
        ventana = new JFrame("Juego De Memoria");
        ventana.setSize(600, 600);
        ventana.setLayout(null);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setLocationRelativeTo(null);
        ventana.setResizable(false);
        
        //JPanel presentacion
        panelPresentacion = new JPanel();
        panelPresentacion.setSize(ventana.getWidth(), ventana.getHeight());
        panelPresentacion.setLocation(0, 0);
        panelPresentacion.setLayout(null);
        panelPresentacion.setVisible(true);
        
        
        //fondoPresentacion
        fondoPresentacion = new JLabel();
        fondoPresentacion.setSize(ventana.getWidth(), ventana.getHeight());
        fondoPresentacion.setLocation(0, 0);
        fondoPresentacion.setIcon(new ImageIcon("imagenes/portada.jpg"));
        fondoPresentacion.setVisible(true);
        panelPresentacion.add(fondoPresentacion,0);
       
        
        //boton de jugar
        BotonJugar = new JLabel();
        BotonJugar.setSize(382, 225);
        BotonJugar.setLocation(48, 0);
        BotonJugar.setIcon(new ImageIcon("imagenes/boton.jpg"));
        BotonJugar.setVisible(true);
        panelPresentacion.add(BotonJugar,0);
        

        //JPanel Juego
        panelJuego = new JPanel();
        panelJuego.setSize(ventana.getWidth(), ventana.getHeight());
        panelJuego.setLocation(0, 0);
        panelJuego.setLayout(null);
        panelJuego.setVisible(true);
        
         
        //matriz logica 
        mat = new int [4][5];
        aleatorio = new Random();
        this.numerosAleatorios();
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 5; j++){
                System.out.println(mat[i][j]+" ");
                
            }
            System.out.println("");
        }
        
        BotonJugar.addMouseListener(new MouseAdapter(){
            public void mousePressd(MouseEvent e){
                //System.out.println("presione el boton");
            
          
        
        
            }});
        
        
        ventana.add(panelPresentacion);
        ventana.setVisible(true);
        
    }
    
    public void numerosAleatorios(){
        
        int acumulador = 0;
        for(int i = 0; i < 4; i++)
            for(int j = 0; i < 5; j++){
                mat[i][j] = 0;
                matAux[i][j] == 0;
            }
        
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 5; j++){
                mat[i][j]= aleatorio.nextInt(10)+1;
                do{
                    acumulador = 0;
                    for(int k = 0; k < 4; k++){
                        for(int l = 0; l < 5; l++){
                            if( mat[i][j] == mat[k][l] ) {
                                acumulador +=1;
                            }
                    
                        }
                    }
                    if(acumulador == 3){
                        mat[i][j]= aleatorio.nextInt(10)+1;
                    }
                }while( acumulador == 3);
                
            }
        
        }
        
        /*for(int i = 0; i < 4; i++){
            for(int j = 0; j < 5; j++){
                System.out.println(mat[i][j]+" ");
                
            }
            System.out.println("");
        }*/
    
    }
    
    
}

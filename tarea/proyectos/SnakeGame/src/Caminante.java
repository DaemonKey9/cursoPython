
import java.util.logging.Level;
import java.util.logging.Logger;


public class Caminante implements Runnable{

    PanelSnake panel;
    boolean estado=true;
    
    public Caminante(PanelSnake panel){
    
    }
    
   
    @Override
    public void run() {
        while(estado){
            panel.avanzar();
            panel.repaint();
            try {
                Thread.sleep(250);
            } catch (InterruptedException ex) {
                Logger.getLogger(Caminante.class.getName()).log(Level.SEVERE, null, ex);
              }
        }
    }
   
    public void para(){
        this.estado=false;
    }
    
}

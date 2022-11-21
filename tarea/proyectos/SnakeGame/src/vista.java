
import java.awt.event.KeyEvent;

public class vista extends javax.swing.JFrame {

    PanelSnake panel;
   
    public vista() {
        initComponents();
        this.setLocationRelativeTo(null);
        
        panel=new PanelSnake(800, 30);
        this.add(panel);
        panel.setBounds(10,10,800,800);
        panel.setOpaque(false);
        
        
        panelfondo fondo = new panelfondo(800,30);
        this.add(fondo);
        fondo.setBounds(10,10,800,800);
        
        this.requestFocus(true);
    }

    
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyPressed(java.awt.event.KeyEvent evt) {
                formKeyPressed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 629, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 505, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void formKeyPressed(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_formKeyPressed
        if(evt.getKeyCode()==KeyEvent.VK_LEFT){
            panel.cambiardireccion("iz");
        }else if(evt.getKeyCode()==KeyEvent.VK_RIGHT){
            panel.cambiardireccion("DE");
        }else if(evt.getKeyCode()==KeyEvent.VK_UP){
            panel.cambiardireccion("ar");
        }else if(evt.getKeyCode()==KeyEvent.VK_DOWN){
            panel.cambiardireccion("ab");
        }    
    }//GEN-LAST:event_formKeyPressed

        
        
    public static void main(String args[]) {
       
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new vista().setVisible(true);
            }
        });
    }
    // Variables declaration - do not modify//GEN-BEGIN:variables
    // End of variables declaration//GEN-END:variables
}

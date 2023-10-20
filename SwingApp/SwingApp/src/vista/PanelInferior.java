package vista;
import java.awt.*;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JPanel;

import utilidades.Rutas;

public class PanelInferior extends JPanel {

	private String stg="";
	private Font font;
	JButton btnConfirmar;
	JButton btnSalir;
	/**
	 * Create the panel.
	 */
	public PanelInferior(boolean visibilidad) {
        font=new Font("Tahoma", Font.PLAIN, 20);
        btnConfirmar=new JButton("Confirmar");
        btnConfirmar.setFont(font);
        btnConfirmar.setVisible(visibilidad);
        btnSalir=new JButton("Salir");
        btnSalir.setFont(font);
        add(btnConfirmar);
        add(btnSalir);
    }
	
	public PanelInferior() {
		
		JButton btnConfirmar = new JButton("CONFIRMAR");
		add(btnConfirmar);
		
		JButton btnSalir = new JButton("SALIR");
		add(btnSalir);

	}
	
	public JButton getbConfirmar() {
        return btnConfirmar;
    }

    public JButton getbSalir() {
        return btnSalir;
    }
    
	public void setStg(String stg) {
		this.stg=stg;
	}
//	public void paintComponent(Graphics g) {
//        super.paintComponent(g);
//        g.drawImage(new ImageIcon(RUTA_IMAGEN_CINCO).getImage(),0,0,getWidth(),600,this);
//        g.setFont(new Font("Roboto", Font.PLAIN, 30));
//        g.setColor(Color.WHITE);
//        g.drawString(stg, 20, 40);
//    }
	public void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2=(Graphics2D)g;
        g2.drawImage(new ImageIcon(Rutas.RUTA_IMAGEN_SEIS).getImage(),0,0,getWidth(),getHeight(),this);
    }
}

package vista;

import static utilidades.Rutas.*;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;

import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class PanelSuperior extends JPanel {

	private String stg="";
	/**
	 * Create the panel.
	 */
	public PanelSuperior() {
		setBackground(Color.WHITE);
		JLabel lblEscuelaMusica = new JLabel("PRODUCTOS");
		lblEscuelaMusica.setFont(new Font("Dialog", Font.BOLD, 30));
		add(lblEscuelaMusica);
	}
	
	public void setStg(String stg) {
		this.stg=stg;
	}
	public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(new ImageIcon(RUTA_IMAGEN_SEIS).getImage(),0,0,getWidth(),600,this);
        g.setFont(new Font("Roboto", Font.PLAIN, 30));
        g.setColor(Color.WHITE);
        g.drawString(stg, 20, 40);
    }


}

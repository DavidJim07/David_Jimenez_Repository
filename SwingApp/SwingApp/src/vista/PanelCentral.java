package vista;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Cursor;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JSeparator;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import java.awt.SystemColor;

public class PanelCentral extends JPanel {
	private JTextField txtIngreseSuNombre;
	private JPasswordField passwordField;
	ImageIcon imanadir;
	Icon iconnadir;
	private JPanel panelBarra;
	private JLabel botonX;
	private JPanel panel;
	private JLabel lblEntrar;
	private JFrame mainContainer;
	private Logo logo;

	/**
	 * Create the panel.
	 */
	public PanelCentral(Logo logo) {
		this.logo=logo;
		setForeground(new Color(128,128,128));
		setBackground(Color.WHITE);
		setSize(new Dimension(800, 500));
		setLayout(null);
		
		panelBarra = new JPanel();
		panelBarra.addMouseMotionListener(new MouseMotionAdapter() {
			@Override
			public void mouseDragged(MouseEvent e) {
				int x=e.getXOnScreen();
				int y=e.getXOnScreen();
			}
		});
		panelBarra.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				
			}
		});
		
		panel = new JPanel();
		panel.setBackground(Color.WHITE);
		panel.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseEntered(MouseEvent e) {
				panel.setBackground(new Color(255, 225, 0));
				lblEntrar.setForeground(new Color(255, 30, 0));
			}
			@Override
			public void mouseExited(MouseEvent e) {
				panel.setBackground(Color.WHITE);
				lblEntrar.setForeground(new Color(255, 30, 0));
			}
			@Override
			public void mouseClicked(MouseEvent e) {
				logo.dispose();
				Ventana.main(new String[] {});
			}
		});
		panel.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
		panel.setBounds(80, 428, 138, 46);
		add(panel);
		panel.setLayout(null);
		
		lblEntrar = new JLabel("Ingresar");
		lblEntrar.setBackground(Color.WHITE);
		lblEntrar.setBounds(10, 11, 106, 25);
		lblEntrar.setForeground(new Color(255, 30, 0));
		panel.add(lblEntrar);
		panelBarra.setBackground(Color.WHITE);
		panelBarra.setBounds(0, 0, 800, 25);
		add(panelBarra);
		panelBarra.setLayout(null);
		
		botonX = new JLabel("X");
		botonX.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
		botonX.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseEntered(MouseEvent e) {
				botonX.setOpaque(true);
				botonX.setBackground(new Color(255, 225, 0));
				botonX.setForeground(new Color(255, 30, 0));
			}
			@Override
			public void mouseExited(MouseEvent e) {
				botonX.setOpaque(true);
				botonX.setBackground(Color.WHITE);
				botonX.setForeground(new Color(255, 30, 0));
			}
			@Override
			public void mouseClicked(MouseEvent e) {
				System.exit(0);
			}
		});
		botonX.setHorizontalAlignment(SwingConstants.CENTER);
		botonX.setForeground(new Color(128, 0, 0));
		botonX.setFont(new Font("Roboto", Font.PLAIN, 30));
		botonX.setBounds(0, 0, 30, 25);
		panelBarra.add(botonX);
		
//		ImageIcon imgIcon = new ImageIcon(getClass().getResource("src/imas/espacio.jpg"));
//        Image imgEscalada = imgIcon.getImage().getScaledInstance(lbImage.getWidth(),
//                lbImage.getHeight(), Image.SCALE_SMOOTH);
//        Icon iconoEscalado = new ImageIcon(imgEscalada);
		
		JLabel lblNewLabel_1 = new JLabel("");
		lblNewLabel_1.setBounds(433, 25, 357, 181);
		add(lblNewLabel_1);
		ImageIcon imgIcon = new ImageIcon(getClass().getResource("/imas/Logo2.jpg"));
        Image imgEscalada = imgIcon.getImage().getScaledInstance(lblNewLabel_1.getWidth(),lblNewLabel_1.getHeight(), Image.SCALE_SMOOTH);
        Icon iconoEscalado = new ImageIcon(imgEscalada);
		lblNewLabel_1.setIcon(iconoEscalado);
		add(lblNewLabel_1);
		
		JLabel lblNewLabel = new JLabel("");
		lblNewLabel.setBounds(483, 217, 288, 273);
		add(lblNewLabel);
		ImageIcon imgIcon2 = new ImageIcon(getClass().getResource("/imas/LosPollosHermanos3.jpg"));
        Image imgEscalada2 = imgIcon2.getImage().getScaledInstance(lblNewLabel.getWidth(),lblNewLabel.getHeight(), Image.SCALE_SMOOTH);
        Icon iconoEscalado2 = new ImageIcon(imgEscalada2);
		lblNewLabel.setIcon(iconoEscalado2);
		add(lblNewLabel);
		
		JLabel lblNewLabel_2 = new JLabel("Logo");
		lblNewLabel_2.setFont(new Font("Roboto", Font.PLAIN, 30));
		lblNewLabel_2.setBounds(221, 63, 115, 36);
		add(lblNewLabel_2);
		
		txtIngreseSuNombre = new JTextField();
		txtIngreseSuNombre.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				if(txtIngreseSuNombre.getText().isEmpty() || txtIngreseSuNombre.getText().isBlank()) {
					txtIngreseSuNombre.setText("Ingrese nombre de usuario");
				}else {
					txtIngreseSuNombre.setText("");
					txtIngreseSuNombre.setForeground(new Color(89,150,90,89));
				}
			}
		});
		txtIngreseSuNombre.setForeground(new Color(128, 128, 128));
		txtIngreseSuNombre.setBackground(SystemColor.inactiveCaptionBorder);
		txtIngreseSuNombre.setText("Ingrese su nombre de usuario");
		txtIngreseSuNombre.setToolTipText("");
		txtIngreseSuNombre.setFont(new Font("Roboto", Font.PLAIN, 14));
		txtIngreseSuNombre.setBounds(80, 244, 256, 36);
		txtIngreseSuNombre.setBorder(null);
		txtIngreseSuNombre.setColumns(10);
		add(txtIngreseSuNombre);
		
		passwordField = new JPasswordField();
		passwordField.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				passwordField.setText("");
				passwordField.setForeground(new Color(74,19,10,37));
			}
		});
		passwordField.setBackground(SystemColor.inactiveCaptionBorder);
		passwordField.setEchoChar('*');
		passwordField.setText("******************");
		passwordField.setFont(new Font("Roboto", Font.PLAIN, 14));
		passwordField.setBounds(80, 351, 256, 36);
		passwordField.setBorder(null);
		add(passwordField);
		
		JLabel lblNewLabel_3 = new JLabel("Usuario");
		lblNewLabel_3.setForeground(new Color(128, 128, 128));
		lblNewLabel_3.setFont(new Font("Roboto", Font.PLAIN, 25));
		lblNewLabel_3.setBounds(80, 203, 106, 30);
		add(lblNewLabel_3);
		
		JLabel lblNewLabel_4 = new JLabel("Contrase�a");
		lblNewLabel_4.setForeground(new Color(128, 128, 128));
		lblNewLabel_4.setFont(new Font("Roboto", Font.PLAIN, 22));
		lblNewLabel_4.setBounds(80, 310, 126, 30);
		add(lblNewLabel_4);
		
		JLabel lblNewLabel_5 = new JLabel("");
		lblNewLabel_5.setBounds(80, 42, 126, 91);
		add(lblNewLabel_5);
		ImageIcon imgIcon3 = new ImageIcon(getClass().getResource("/imas/LosPollosHermanos.png"));
        Image imgEscalada3 = imgIcon3.getImage().getScaledInstance(lblNewLabel_5.getWidth(),lblNewLabel_5.getHeight(), Image.SCALE_SMOOTH);
        Icon iconoEscalado3 = new ImageIcon(imgEscalada3);
        lblNewLabel_5.setIcon(iconoEscalado3);
        
//        JButton btnNewButton = new JButton("Entrar");
//        btnNewButton.setForeground(new Color(0, 0, 0));
//        btnNewButton.setBackground(new Color(0, 51, 204));
//        btnNewButton.setFont(new Font("Roboto", Font.PLAIN, 22));
//        btnNewButton.setBounds(80, 444, 154, 36);
//        add(btnNewButton);
        
        JLabel lblNewLabel_6 = new JLabel("Iniciar Sesi�n");
        lblNewLabel_6.setFont(new Font("Roboto", Font.PLAIN, 26));
        lblNewLabel_6.setBounds(80, 164, 183, 28);
        add(lblNewLabel_6);
        
        JSeparator separator = new JSeparator();
        separator.setBackground(SystemColor.activeCaption);
        separator.setBounds(80, 291, 256, 19);
        add(separator);
        
        JSeparator separator_1 = new JSeparator();
        separator_1.setBackground(SystemColor.activeCaption);
        separator_1.setBounds(80, 398, 256, 19);
        add(separator_1);
		
	}
}

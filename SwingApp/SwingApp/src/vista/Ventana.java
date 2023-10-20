package vista;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.rmi.AccessException;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.border.EmptyBorder;

import interfaz.Operable;
import interfaz.ServiceImplementation;
import modelo.Producto;
import utilidades.Options;
import utilidades.Rutas;

//import utilidades.Options.*;

public class Ventana extends JFrame implements ActionListener{

	private JPanel contentPane;
	private JMenu menuProductos;
	private JMenu menuVentas;
	private JMenu menuInventario;
	private JMenu menuHistorial;
	private JMenu menuHelp;
	private JButton btnConfirmar;
	private JButton btnSalir;
    private PanelCentralListar panelCentralListar;
	private Operable service;
	private JMenuItem opRegistrarProducto;
	private JMenuItem opConsultarProducto;
	private JMenuItem opModificarProducto;
	private JMenuItem opElimimarProducto;
	private JMenuItem opOrdenarProducto;
	private JMenuItem opListarProducto;
	private JMenuItem opAbout;
	private JMenuItem opAccionesFaltantes;
	private PanelSuperior panelSuperior;
	private PanelInferior panelInferior;
	private PanelCentralInsertar panelCentralInsertar;
	private JScrollPane scrollPanelCentralInsertar;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Ventana frame = new Ventana();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Ventana() {
		try {
			service = new ServiceImplementation();
			setIconImage(Toolkit.getDefaultToolkit().getImage(Ventana.class.getResource("/imas/dm 150.jpg")));
			setTitle("GUI CIENCIA Y TECNOLOGIA");
			setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			setBounds(200, 100, 800, 500);

			JMenuBar menuBar = new JMenuBar();
			setJMenuBar(menuBar);

			menuProductos = new JMenu(Options.OPCION_PRODUCTOS);
			menuBar.add(menuProductos);

			opRegistrarProducto = new JMenuItem(Options.OPCION_AGREGAR);
			OyenteRegistrarProducto oyenteregistrarproducto= new OyenteRegistrarProducto();
			opRegistrarProducto.addActionListener(oyenteregistrarproducto);
			menuProductos.add(opRegistrarProducto);

			opConsultarProducto = new JMenuItem(Options.OPCION_CONSULTAR);
			opConsultarProducto.addActionListener(new OyenteConsultarProducto());
			menuProductos.add(opConsultarProducto);

			opModificarProducto = new JMenuItem(Options.OPCION_MODIFICAR);
			ActionListener oyentemodificar= new OyenteModificarProducto();
			opModificarProducto.addActionListener(oyentemodificar);
			menuProductos.add(opModificarProducto);

			opElimimarProducto = new JMenuItem(Options.OPCION_ELIMINAR);
			opElimimarProducto.addActionListener(this);
			menuProductos.add(opElimimarProducto);

			opOrdenarProducto = new JMenuItem(Options.OPCION_ORDENAR);
			opOrdenarProducto.addActionListener(new ActionListener(){
				@Override
				public void actionPerformed(ActionEvent e) {
					JOptionPane.showMessageDialog(null, "Me diste Click ordenar");
				}
			});
			menuProductos.add(opOrdenarProducto);

			opListarProducto = new JMenuItem(Options.OPCION_LISTAR);
//			opListarProducto.addActionListener(e->JOptionPane.showMessageDialog(null, "Me diste Click Listar"));
			OyenteBotonListar oyenteListarproducto= new OyenteBotonListar();
			opListarProducto.addActionListener(oyenteListarproducto);
			menuProductos.add(opListarProducto);

			menuVentas = new JMenu(Options.OPCION_VENTAS);
			menuBar.add(menuVentas);

			menuInventario = new JMenu(Options.OPCION_INVENTARIO);
			menuBar.add(menuInventario);

			menuHistorial = new JMenu(Options.OPCION_HISTORIAL);
			menuBar.add(menuHistorial);

			menuHelp = new JMenu(Options.OPCION_HELP);
			menuBar.add(menuHelp);
			
			opAbout = new JMenuItem("About... Datos");
			String mensaje="Realizó: David Jiménez De Jesús - 19651168\n(Alumno de Tópicos Avanzados de Programación)\n\nPrograma hecho en la semana de la ciencia y tecnología del taller de: \n'Implementación de"
					+ " GUI y acceso a Datos con Java'\n\nImpartido por el docente: José Alfredo Jiménez Meza";
			opAbout.addActionListener(new ActionListener(){
				@Override
				public void actionPerformed(ActionEvent e) {
					JOptionPane.showMessageDialog(null, mensaje);
				}
			});
			menuHelp.add(opAbout);
			opAccionesFaltantes = new JMenuItem("Acciones Faltantes");
			opAccionesFaltantes.addActionListener(new ActionListener(){
				@Override
				public void actionPerformed(ActionEvent e) {
					JOptionPane.showMessageDialog(null, "1.-Unicamente la acción de que cuando se inicia\nel proceso de agregar, el cursor se situe en el\n campo de 'Codigo de barras'.");
				}
			});
			menuHelp.add(opAccionesFaltantes);
			
			contentPane = new JPanel() {
				@Override
				public void paintComponent(Graphics g) {
					super.paintComponent(g);
					Image imagenFondo=new ImageIcon(Rutas.RUTA_IMAGEN_SEIS).getImage();
					g.drawImage(imagenFondo,0,0,getWidth(),getHeight(),this);
				}
			};

			contentPane.setLayout(new BorderLayout());
			contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
			setContentPane(contentPane);

			panelSuperior=new PanelSuperior();
			contentPane.add(panelSuperior, BorderLayout.NORTH);
			//			panelInferior=new PanelInferior();
			//			contentPane.add(panelInferior, BorderLayout.SOUTH);


			setVisible(true);
		} catch (AccessException e) {
			JOptionPane.showMessageDialog(null, e.getMessage());
		}
	}

	private class OyenteRegistrarProducto implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			if (btnSalir!=null) {
				btnSalir.doClick();
			}
			panelCentralInsertar = new PanelCentralInsertar();
//			panelCentralInsertar.codigoBarras.requestFocus();
//			System.out.println(panelCentralInsertar.focus());
			scrollPanelCentralInsertar = new JScrollPane(panelCentralInsertar);
			opRegistrarProducto.setEnabled(false);
			panelInferior = new PanelInferior(true);
			
			btnConfirmar=panelInferior.getbConfirmar();
			btnConfirmar.addActionListener(new OyenteBotonConfirmar());
			btnSalir=panelInferior.getbSalir();
			btnSalir.addActionListener(new OyenteBotonSalir());
			contentPane.add(scrollPanelCentralInsertar,BorderLayout.CENTER);
			contentPane.add(panelInferior, BorderLayout.SOUTH);
			panelSuperior.setStg("Agregar");
			revalidate();


		}
	}
	
	private class OyenteBotonSalir implements ActionListener{         
		@Override        
		public void actionPerformed(ActionEvent e) {            
			panelSuperior.setStg("");            
			if(opRegistrarProducto.isEnabled()==false) {                
				scrollPanelCentralInsertar.setVisible(false);                
				contentPane.remove(scrollPanelCentralInsertar);                
				panelCentralInsertar=null;                
				scrollPanelCentralInsertar=null;                
				opRegistrarProducto.setEnabled(true);            
			}            
			if(opListarProducto.isEnabled()==false) { 
				panelCentralListar.setVisible(false);                
				contentPane.remove(panelCentralListar);                
				panelCentralInsertar=null;                
				opListarProducto.setEnabled(true);            
			}                        
			if (panelInferior!=null) {                
				panelInferior.setVisible(false);                
				contentPane.remove(panelInferior);                
				panelInferior=null;            
			}                        
			System.gc();            
			repaint();         
		}     
	}

	private class OyenteBotonConfirmar implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			try {
				Producto producto=panelCentralInsertar.getProducto();
				JOptionPane.showMessageDialog(null, service.guardar(producto));
			} catch (Exception e2) {
				// TODO: handle exception
				JOptionPane.showMessageDialog(null, "Ocurrio un error\n"+e2.getMessage());
			}
			
		}
	}
	
	private class OyenteBotonListar implements ActionListener{
        @Override
        public void actionPerformed(ActionEvent e) {
            if (btnSalir!=null) {
            	btnSalir.doClick();
            }
            panelCentralListar=new PanelCentralListar(service);
            opListarProducto.setEnabled(false);
            panelInferior=new PanelInferior(false);
            btnSalir=panelInferior.getbSalir();
            btnSalir.addActionListener(new OyenteBotonSalir());
            contentPane.add(panelCentralListar,BorderLayout.CENTER);
            contentPane.add(panelInferior,BorderLayout.SOUTH);
            //panelSuperior.setOpcionSeleccionada("Listar");
            revalidate();
        }
    }

	private class OyenteConsultarProducto implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			JOptionPane.showMessageDialog(null, "Me diste Click consultar");
		}
	}

	private class OyenteModificarProducto implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			JOptionPane.showMessageDialog(null, "Me diste Click modificar");
		}
	}

//	private class OyenteEliminarProducto implements ActionListener{
//		@Override
//		public void actionPerformed(ActionEvent e) {
//			JOptionPane.showMessageDialog(null, "Me diste Click eliminar");
//		}
//	}

	@Override
	public void actionPerformed(ActionEvent evento) {
		JMenuItem item = (JMenuItem)evento.getSource();
		if(item==opElimimarProducto) {
			JOptionPane.showMessageDialog(null, "Me diste Click eliminar");
		}
		if(item==opOrdenarProducto) {
			JOptionPane.showMessageDialog(null, "Me diste Click ordenar");
		}


	}

}

package vista;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ComponentListener;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.rmi.AccessException;
import java.util.EventObject;
import java.util.Random;

import javax.swing.*;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;

import com.mysql.cj.protocol.a.result.ResultsetRowsCursor;

import interfaz.Operable;
import interfaz.ServiceImplementation;
import modelo.Producto;

public class PanelCentralInsertar extends JPanel {
	private JLabel codigoDeBarras;
	private JLabel stockMaximo;
	private JLabel nombreProducto;
	private JLabel stockMinimo;
	private JLabel marcaProducto;
	private JLabel precioVenta;
	private JLabel tipoProducto;
	private JLabel precioCompra;
	private JLabel contenidoProducto;
	private JLabel presentacion;
	private JLabel unidadMedida;
	private JLabel descripcion;
	private JTextField presentacionProd;
	private JTextField contenidoProd;
	private JTextField unidadProd;
	private JTextField precioCom;
	private JTextField descripcionProd;
	private JTextField codigoBarras;
	private JTextField stockMax;
	private JTextField nombreProd;
	private JTextField stockMin;
	private JTextField marcaProd;
	private JTextField precioVen;
	private JTextField tipoProd;
	private PanelInferior panelInferior;
	private Operable service;
	//private ServiceImplementation service;

	/**
	 * Create the panel.
	 */
	public PanelCentralInsertar() {
		try {
			service = new ServiceImplementation();
			setBackground(new Color(255, 160, 0));
			setForeground(new Color(255, 225, 0));
			setLayout(new GridLayout(6, 4, 0, 50));
			
			codigoDeBarras = new JLabel("Codigo de Barras");
			codigoDeBarras.setForeground(new Color(102, 0, 0));
			codigoDeBarras.setHorizontalTextPosition(SwingConstants.CENTER);
			codigoDeBarras.setHorizontalAlignment(SwingConstants.CENTER);
			codigoDeBarras.setFont(new Font("Rasa", Font.BOLD, 30));
			codigoDeBarras.setAutoscrolls(true);
			codigoDeBarras.setAlignmentX(Component.RIGHT_ALIGNMENT);
			add(codigoDeBarras);
			
			codigoBarras = new JTextField();
			codigoBarras.addKeyListener(new KeyAdapter() {
				@Override
				public void keyTyped(KeyEvent e) {
					//System.out.println(e.getKeyChar());
					String codigo=codigoBarras.getText();
					if(!Character.isDigit(e.getKeyChar())) {
						e.consume();
					}
					if(codigo.length()>12) {
						e.consume();
						if(service.verificarExistencia(codigo)) {
							JOptionPane.showMessageDialog(null, "Este codigo de barras ya existe, prueba con otro diferente");
							codigoBarras.setText("");
							codigoBarras.requestFocus();
						}else { nombreProd.requestFocus();}
					}

				}
			});
			codigoBarras.setFont(new Font("Rasa", Font.BOLD, 15));
			add(codigoBarras);
			codigoBarras.setColumns(10);
			
			stockMaximo = new JLabel("Stock Maximo");
			stockMaximo.setForeground(new Color(102, 0, 0));
			stockMaximo.setHorizontalTextPosition(SwingConstants.CENTER);
			stockMaximo.setHorizontalAlignment(SwingConstants.CENTER);
			stockMaximo.setFont(new Font("Rasa", Font.BOLD, 30));
			add(stockMaximo);
			
			stockMax = new JTextField();
			stockMax.setFont(new Font("Rasa", Font.BOLD, 15));
			stockMax.addKeyListener(new KeyListener() {
		        @Override
		        public void keyTyped(KeyEvent e) { }

		        @Override
		        public void keyPressed(KeyEvent e) {
		            if (e.getKeyCode() == KeyEvent.VK_ENTER) {
		                stockMin.requestFocus();
		            }
		        }

		        @Override
		        public void keyReleased(KeyEvent e) { }
		    });
			add(stockMax);
			stockMax.setColumns(10);
			
			nombreProducto = new JLabel("Nombre producto");
			nombreProducto.setForeground(new Color(102, 0, 0));
			nombreProducto.setHorizontalTextPosition(SwingConstants.CENTER);
			nombreProducto.setHorizontalAlignment(SwingConstants.CENTER);
			nombreProducto.setFont(new Font("Rasa", Font.BOLD, 30));
			add(nombreProducto);
			
			nombreProd = new JTextField();
			nombreProd.setFont(new Font("Rasa", Font.BOLD, 15));
			nombreProd.addKeyListener(new KeyListener() {
		        @Override
		        public void keyTyped(KeyEvent e) { }

		        @Override
		        public void keyPressed(KeyEvent e) {
		            if (e.getKeyCode() == KeyEvent.VK_ENTER) {
		                marcaProd.requestFocus();
		            }
		        }

		        @Override
		        public void keyReleased(KeyEvent e) { }
		    });
			add(nombreProd);
			nombreProd.setColumns(10);
			
			stockMinimo = new JLabel("Stock Minimo");
			stockMinimo.setForeground(new Color(102, 0, 0));
			stockMinimo.setHorizontalTextPosition(SwingConstants.CENTER);
			stockMinimo.setHorizontalAlignment(SwingConstants.CENTER);
			stockMinimo.setFont(new Font("Rasa", Font.BOLD, 30));
			add(stockMinimo);
			
			stockMin = new JTextField();
			stockMin.setFont(new Font("Rasa", Font.BOLD, 15));
			stockMin.addKeyListener(new KeyListener() {
		        @Override
		        public void keyTyped(KeyEvent e) { }

		        @Override
		        public void keyPressed(KeyEvent e) {
		            if (e.getKeyCode() == KeyEvent.VK_ENTER) {
		                precioVen.requestFocus();
		            }
		        }

		        @Override
		        public void keyReleased(KeyEvent e) { }
		    });
			add(stockMin);
			stockMin.setColumns(10);
			
			marcaProducto = new JLabel("Marca producto");
			marcaProducto.setForeground(new Color(102, 0, 0));
			marcaProducto.setHorizontalTextPosition(SwingConstants.CENTER);
			marcaProducto.setHorizontalAlignment(SwingConstants.CENTER);
			marcaProducto.setFont(new Font("Rasa", Font.BOLD, 30));
			add(marcaProducto);
			
			marcaProd = new JTextField();
			marcaProd.setFont(new Font("Rasa", Font.BOLD, 15));
			marcaProd.addKeyListener(new KeyListener() {
		        @Override
		        public void keyTyped(KeyEvent e) { }

		        @Override
		        public void keyPressed(KeyEvent e) {
		            if (e.getKeyCode() == KeyEvent.VK_ENTER) {
		                tipoProd.requestFocus();
		            }
		        }

		        @Override
		        public void keyReleased(KeyEvent e) { }
		    });
			add(marcaProd);
			marcaProd.setColumns(10);
			
			precioVenta = new JLabel("Precio Venta");
			precioVenta.setForeground(new Color(102, 0, 0));
			precioVenta.setHorizontalTextPosition(SwingConstants.CENTER);
			precioVenta.setHorizontalAlignment(SwingConstants.CENTER);
			precioVenta.setFont(new Font("Rasa", Font.BOLD, 30));
			add(precioVenta);
			
			precioVen = new JTextField();
			precioVen.setFont(new Font("Rasa", Font.BOLD, 15));
			precioVen.addKeyListener(new KeyListener() {
		        @Override
		        public void keyTyped(KeyEvent e) { }

		        @Override
		        public void keyPressed(KeyEvent e) {
		            if (e.getKeyCode() == KeyEvent.VK_ENTER) {
		                precioCom.requestFocus();
		            }
		        }

		        @Override
		        public void keyReleased(KeyEvent e) { }
		    });
			add(precioVen);
			precioVen.setColumns(10);
			
			tipoProducto = new JLabel("Tipo Producto");
			tipoProducto.setForeground(new Color(102, 0, 0));
			tipoProducto.setHorizontalTextPosition(SwingConstants.CENTER);
			tipoProducto.setHorizontalAlignment(SwingConstants.CENTER);
			tipoProducto.setFont(new Font("Rasa", Font.BOLD, 30));
			add(tipoProducto);
			
			tipoProd = new JTextField();
			tipoProd.setFont(new Font("Rasa", Font.BOLD, 15));
			tipoProd.addKeyListener(new KeyListener() {
		        @Override
		        public void keyTyped(KeyEvent e) { }

		        @Override
		        public void keyPressed(KeyEvent e) {
		            if (e.getKeyCode() == KeyEvent.VK_ENTER) {
		                contenidoProd.requestFocus();
		            }
		        }

		        @Override
		        public void keyReleased(KeyEvent e) { }
		    });
			add(tipoProd);
			tipoProd.setColumns(10);
			
			precioCompra = new JLabel("Precio Compra");
			precioCompra.setForeground(new Color(102, 0, 0));
			precioCompra.setHorizontalTextPosition(SwingConstants.CENTER);
			precioCompra.setHorizontalAlignment(SwingConstants.CENTER);
			precioCompra.setFont(new Font("Rasa", Font.BOLD, 30));
			add(precioCompra);
			
			precioCom = new JTextField();
			precioCom.setFont(new Font("Rasa", Font.BOLD, 15));
			precioCom.addKeyListener(new KeyListener() {
		        @Override
		        public void keyTyped(KeyEvent e) { }

		        @Override
		        public void keyPressed(KeyEvent e) {
		            if (e.getKeyCode() == KeyEvent.VK_ENTER) {
		            	presentacionProd.requestFocus();
		            }
		        }

		        @Override
		        public void keyReleased(KeyEvent e) { }
		    });
			add(precioCom);
			precioCom.setColumns(10);
			
			contenidoProducto = new JLabel("Contenido Producto");
			contenidoProducto.setForeground(new Color(102, 0, 0));
			contenidoProducto.setHorizontalTextPosition(SwingConstants.CENTER);
			contenidoProducto.setHorizontalAlignment(SwingConstants.CENTER);
			contenidoProducto.setFont(new Font("Rasa", Font.BOLD, 30));
			add(contenidoProducto);
			
			contenidoProd = new JTextField();
			contenidoProd.setFont(new Font("Rasa", Font.BOLD, 15));
			contenidoProd.addKeyListener(new KeyListener() {
		        @Override
		        public void keyTyped(KeyEvent e) { }

		        @Override
		        public void keyPressed(KeyEvent e) {
		            if (e.getKeyCode() == KeyEvent.VK_ENTER) {
		                unidadProd.requestFocus();
		            }
		        }

		        @Override
		        public void keyReleased(KeyEvent e) { }
		    });
			add(contenidoProd);
			contenidoProd.setColumns(10);
			
			presentacion = new JLabel("Presentacion");
			presentacion.setForeground(new Color(102, 0, 0));
			presentacion.setHorizontalTextPosition(SwingConstants.CENTER);
			presentacion.setHorizontalAlignment(SwingConstants.CENTER);
			presentacion.setFont(new Font("Rasa", Font.BOLD, 30));
			add(presentacion);
			
			presentacionProd = new JTextField();
			presentacionProd.setFont(new Font("Rasa", Font.BOLD, 15));
			presentacionProd.addKeyListener(new KeyListener() {
		        @Override
		        public void keyTyped(KeyEvent e) { }

		        @Override
		        public void keyPressed(KeyEvent e) {
		            if (e.getKeyCode() == KeyEvent.VK_ENTER) {
		                descripcionProd.requestFocus();
		            }
		        }

		        @Override
		        public void keyReleased(KeyEvent e) { }
		    });
			add(presentacionProd);
			presentacionProd.setColumns(10);
			
			unidadMedida = new JLabel("Unidad de medida");
			unidadMedida.setForeground(new Color(102, 0, 0));
			unidadMedida.setHorizontalTextPosition(SwingConstants.CENTER);
			unidadMedida.setHorizontalAlignment(SwingConstants.CENTER);
			unidadMedida.setFont(new Font("Rasa", Font.BOLD, 30));
			add(unidadMedida);
			
			unidadProd = new JTextField();
			unidadProd.setFont(new Font("Rasa", Font.BOLD, 15));
			unidadProd.addKeyListener(new KeyListener() {
		        @Override
		        public void keyTyped(KeyEvent e) { }

		        @Override
		        public void keyPressed(KeyEvent e) {
		            if (e.getKeyCode() == KeyEvent.VK_ENTER) {
		                stockMax.requestFocus();
		            }
		        }

		        @Override
		        public void keyReleased(KeyEvent e) { }
		    });
			add(unidadProd);
			unidadProd.setColumns(10);
			
			descripcion = new JLabel("Descripción Producto");
			descripcion.setForeground(new Color(102, 0, 0));
			descripcion.setHorizontalTextPosition(SwingConstants.CENTER);
			descripcion.setHorizontalAlignment(SwingConstants.CENTER);
			descripcion.setFont(new Font("Rasa", Font.BOLD, 30));
			add(descripcion);
			
			descripcionProd = new JTextField();
			descripcionProd.setFont(new Font("Rasa", Font.BOLD, 15));
			add(descripcionProd);
			descripcionProd.setColumns(10);
		} catch (AccessException e) {
			JOptionPane.showMessageDialog(null, e.getMessage());
		}
	}
	
//	public boolean focus() {
//		codigoBarras.isRequestFocusEnabled();
//		if (codigoBarras.requestFocusInWindow()) {
//			return true;
//		}else {
//			return false;
//		}
//	}
	
	public Producto getProducto() {
		try {
			Producto producto = new Producto();
			producto.setCodigoBarra(codigoBarras.getText());
			producto.setNombre(nombreProd.getText());
			producto.setMarca(marcaProd.getText());
			producto.setTipo(tipoProd.getText());
			producto.setContenido(contenidoProd.getText());
			producto.setUnidadMedida(unidadProd.getText());
			producto.setCantidadProducto((int)(Math.random()*30+1));
			producto.setStockMinimo(Integer.parseInt(stockMin.getText()));
			producto.setStockMaximo(Integer.parseInt(stockMax.getText()));
			producto.setPrecioVenta(Float.parseFloat(precioVen.getText()));
			producto.setPrecioCompra(Float.parseFloat(precioCom.getText()));
			producto.setPresentacion(presentacionProd.getText());
			producto.setDescripcion(descripcionProd.getText());
			return producto;
		} catch (NumberFormatException e) {
			JOptionPane.showMessageDialog(null, "No puedes dejar espacios en blanco");
			return null;
		}
	}
	
}

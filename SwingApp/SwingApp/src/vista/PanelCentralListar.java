package vista;

import java.util.List;
import java.awt.Color;
import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.AbstractTableModel;
import javax.swing.table.TableModel;
import java.awt.BorderLayout;
import interfaz.Operable;
import modelo.Producto;
import java.awt.Graphics;
import java.awt.Graphics2D;

public class PanelCentralListar extends JPanel{



	private JTable tablaProductos;
	private List<Producto> listaProductos;
	
	public static void main(String[] args) {
		try {
			System.out.println();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public PanelCentralListar(Operable service) {
		setLayout(new BorderLayout());

		listaProductos=service.getListProductos();

		TableModel miTabla=new ModeloTablaPersonalizada();

		tablaProductos=new JTable(miTabla);
		tablaProductos.setOpaque(false);
		tablaProductos.setAutoResizeMode(tablaProductos.AUTO_RESIZE_OFF);
		tablaProductos.getColumnModel().getColumn(0).setPreferredWidth(100);
		tablaProductos.getColumnModel().getColumn(1).setPreferredWidth(130);
		tablaProductos.getColumnModel().getColumn(2).setPreferredWidth(100);
		tablaProductos.getColumnModel().getColumn(3).setPreferredWidth(120);
		tablaProductos.getColumnModel().getColumn(4).setPreferredWidth(70);
		tablaProductos.getColumnModel().getColumn(5).setPreferredWidth(100);
		tablaProductos.getColumnModel().getColumn(6).setPreferredWidth(80);
		tablaProductos.getColumnModel().getColumn(7).setPreferredWidth(80);
		tablaProductos.getColumnModel().getColumn(8).setPreferredWidth(80);
		tablaProductos.getColumnModel().getColumn(9).setPreferredWidth(100);
		tablaProductos.getColumnModel().getColumn(10).setPreferredWidth(100);
		tablaProductos.getColumnModel().getColumn(11).setPreferredWidth(110);
		tablaProductos.getColumnModel().getColumn(12).setPreferredWidth(350);

		JScrollPane tablaScroll=new JScrollPane(tablaProductos);
		tablaScroll.getViewport().setBackground(Color.WHITE);
		add(tablaScroll,BorderLayout.CENTER);




	}
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		Graphics2D g2=(Graphics2D)g;
		g2.drawImage(new ImageIcon("src/imas/Pollos.jpg").getImage(),0,0,getWidth(),getHeight(),this);
	}
	
	private class ModeloTablaPersonalizada extends AbstractTableModel{
		private Object[][] datos;
		private int numeroProductos;

		public ModeloTablaPersonalizada() {
			//listaProductos.listIterator();
			numeroProductos=listaProductos.size();
			matrizProductos();
		}



		@Override
		public int getRowCount() {
			return numeroProductos;
		}



		@Override
		public int getColumnCount() {
			return 13;
		}



		@Override
		public Object getValueAt(int rowIndex, int columnIndex) {
			return datos[rowIndex][columnIndex];



		}
		public void matrizProductos() {
			datos=new Object[numeroProductos][13];
			for (int i = 0; i < numeroProductos; i++){ 
				//int x=0;
				String codigoBarra = listaProductos.get(i).getCodigoBarra(); 
				String nombre = listaProductos.get(i).getNombre();
				String marca =listaProductos.get(i).getMarca(); 
				String tipo = listaProductos.get(i).getTipo(); 
				String contenido = listaProductos.get(i).getContenido(); 
				String unidadMedida = listaProductos.get(i).getUnidadMedida();
				int cantidadProductos =listaProductos.get(i).getCantidadProducto();
				int max = listaProductos.get(i).getStockMaximo(); 
				int min =listaProductos.get(i).getStockMinimo(); 
				double pVenta = listaProductos.get(i).getPrecioVenta();
				double pCompra = listaProductos.get(i).getPrecioCompra(); 
				String presentacion = listaProductos.get(i).getPresentacion();
				String descripcion = listaProductos.get(i).getDescripcion(); 
				datos[i][0]=codigoBarra;
				datos[i][1]=nombre;
				datos[i][2]=marca;
				datos[i][3]=tipo;
				datos[i][4]=contenido;
				datos[i][5]=unidadMedida;
				datos[i][6]=cantidadProductos;
				datos[i][7]=max;
				datos[i][8]=min;
				datos[i][9]=pVenta;
				datos[i][10]=pCompra;
				datos[i][11]=presentacion;
				datos[i][12]=descripcion;
			}
		}



		private String[] atributosNom= {"Código de Barra","Nombre","Marca","Tipo","Contenido","Unidad de Medida","En Existencia","Stock Máximo","Stock Mínimo","Precio de Venta","Precio de Compra","Presentación","Descripción"};
		public String getColumnName(int c) {
			return atributosNom[c];
		}
	}
}


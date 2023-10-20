package dao;
import java.rmi.AccessException;
import java.util.List;

import interfaz.Operable;
import interfaz.ServiceImplementation;
import modelo.Producto;


public class Prueba {

	public static void main(String[] args) {
		BaseDatos baseDatos = BaseDatos.newInstance("Producto?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC", 
				"root", "lobito200", "jdbc:mysql://localhost/", "com.mysql.cj.jdbc.Driver");
		System.out.println(baseDatos.hacerConexion());

		TablaProductos tablaProductos=new TablaProductos(baseDatos.getConexion());
//		Producto producto=new Producto();
//	    producto.setCodigoBarra("1111111111117");        
//	    producto.setNombre("Leche Deslactosada");        
//	    producto.setMarca("Lala");
//	    producto.setTipo("Alimento");
//	    producto.setContenido("500");
//	    producto.setUnidadMedida("Mililitros");
//	    producto.setCantidadProducto(10);
//	    producto.setStockMaximo(25);
//	    producto.setStockMinimo(15);
//	    producto.setPrecioVenta(25);
//	    producto.setPrecioCompra(19);
//	    producto.setPresentacion("Caja");
//	    producto.setDescripcion("Leche light");
//	    System.out.println("Datos en tabla");
//	    System.out.println(tablaProductos.guardar(producto));
		List<Producto> productos=tablaProductos.getListProductos();
		System.out.println(productos.size());
		for (Producto producto : productos) {
			System.out.println(producto);
		}
//		Operable service;
//		try {
//			service = new ServiceImplementation();
//			System.out.println(service.verificarExistencia("1111111111117"));
//		} catch (AccessException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
		



	}

}

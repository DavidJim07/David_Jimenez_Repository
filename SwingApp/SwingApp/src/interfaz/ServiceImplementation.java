package interfaz;

import java.rmi.AccessException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import java.util.Properties;
import static utilidades.Utilidad.*;
import dao.BaseDatos;
import dao.TablaProductos;
import modelo.Producto;
import java.sql.Statement;

public class ServiceImplementation implements Operable{
	private BaseDatos baseDatos;
	private Properties properties;
	private TablaProductos tablaProducto;
	private Statement statement;
	private  Connection conexion;
	
	public ServiceImplementation() throws AccessException{
        properties=getProperties();
        baseDatos=BaseDatos.newInstance(properties.get("BASE_DATOS").toString(),
                properties.get("USUARIO").toString(),
                properties.get("CLAVE").toString(),
                properties.get("PROTOCOLO").toString(),
                properties.get("DRIVER").toString());
        if(baseDatos.hacerConexion().equals("exito")) {
            System.out.println("conexion exitosa");
            tablaProducto=new TablaProductos(baseDatos.getConexion());
        }
        else{
            System.out.println("No hay conexion");
            throw new AccessException("Error de acceso a la base de datos");
        }
       
       
    }
	

	@Override
	public String guardar(Producto producto) {
		try {
			statement=baseDatos.getConexion().createStatement();
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		}
		String sql = "insert into producto(codigoBarras,nombreProducto,marcaProducto,tipoProducto,contenidoProducto,unidadMedidaProducto,cantidadProducto, stockMaxProducto,stockMinProducto,precioVentaProducto,precioCompraProducto,presentacionProducto,descripcionProducto) "
				+ "values('"+
				producto.getCodigoBarra()+"','"+
				producto.getNombre()+"','"+
				producto.getMarca()+"','"+
				producto.getTipo()+"','"+
				producto.getContenido()+"','"+
				producto.getUnidadMedida()+"','"+
				producto.getCantidadProducto()+"','"+
				producto.getStockMaximo()+"','"+
				producto.getStockMinimo()+"','"+
				producto.getPrecioVenta()+"','"+
				producto.getPrecioCompra()+"','"+
				producto.getPresentacion()+"','"+
				producto.getDescripcion()+"')";
		try {
            statement.executeUpdate(sql);
            //JOptionPane.showMessageDialog(null, "Ha sido agregado con exito");
            return "Producto registrado con exito";
        } catch(java.sql.SQLIntegrityConstraintViolationException e4) {
            //JOptionPane.showMessageDialog(null, "Ya existe producto con ese codigo de barra");
            return e4.toString();
        }catch (SQLException e) {
            //System.out.println(e.toString());
            return e.toString();
        }
	}

	@Override
	public List<Producto> getListProductos() {
		BaseDatos baseDatos = BaseDatos.newInstance("Producto?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC", 
				"root", "lobito200", "jdbc:mysql://localhost/", "com.mysql.cj.jdbc.Driver");
		System.out.println(baseDatos.hacerConexion());

		TablaProductos tablaProductos=new TablaProductos(baseDatos.getConexion());
		List<Producto> productos=tablaProductos.getListProductos();
		return productos;
//		return null;
	}
	
	@Override
	public boolean verificarExistencia(String filtro) {
		try {
			try {
				statement=baseDatos.getConexion().createStatement();
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
			ResultSet rs = statement.executeQuery("select * from producto where codigoBarras="+filtro);
			//			if(rs.next()==true) {
			//				return true;
			//			}else {
			//				return false;
			//			}
			//System.out.println(rs.next());
			return rs.next()==true?true:false;
		}catch(java.sql.SQLException e) {
			System.out.println("No funciona");
			return false;
		}catch (NullPointerException e) {
			// TODO: handle exception
			System.out.println("Objeto nulo con la clave: "+filtro);
			return false;
		}
		
	}

}

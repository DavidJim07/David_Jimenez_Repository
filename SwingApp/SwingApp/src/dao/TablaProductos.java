package dao;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import modelo.Producto;

public class TablaProductos {

	private  Connection conexion;
	private Statement statement;

	public TablaProductos(Connection conexion) {
		this.conexion = conexion;
		try {
			statement=conexion.createStatement();
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		}
	}

	public String guardar(Producto producto) {
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
	
	public List<Producto> getListProductos(){
        String sql="Select * from producto";
        try {
            ResultSet rs=statement.executeQuery(sql);
            List<Producto> productos=new ArrayList<>();
            //productos.clear();
            while(rs.next()) {
                Producto producto=new Producto();
                producto.setCodigoBarra(rs.getString("codigoBarras"));
                producto.setNombre(rs.getString("nombreProducto"));
                producto.setMarca(rs.getString("marcaProducto"));
                producto.setTipo(rs.getString("tipoProducto"));
                producto.setContenido(rs.getString("contenidoProducto"));
                producto.setUnidadMedida(rs.getString("unidadMedidaProducto"));
                producto.setCantidadProducto(rs.getInt("cantidadProducto"));
                producto.setStockMaximo(rs.getInt("stockMaxProducto"));
                producto.setStockMinimo(rs.getInt("stockMinProducto"));
                producto.setPrecioVenta(rs.getFloat("precioVentaProducto"));
                producto.setPrecioCompra(rs.getFloat("precioCompraProducto"));
                producto.setPresentacion(rs.getString("presentacionProducto"));
                producto.setDescripcion(rs.getString("descripcionProducto"));
                productos.add(producto);

            }
            Collections.sort(productos);
            return productos;
        }catch(SQLException e) {
            System.out.println(e.toString());
            return null;
        }
    }
	
}

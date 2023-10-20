package interfaz;

import java.util.List;
import modelo.Producto;

public interface Operable {
	
	String guardar(Producto producto);
	List<Producto> getListProductos();
	boolean verificarExistencia(String filtro);
	
}


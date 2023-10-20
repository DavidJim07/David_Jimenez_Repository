package modelo;

public class Producto implements Comparable<Producto>{

	private String codigoBarra;
	private String nombre;
	private  String marca;
	private String tipo;
	private String contenido;
	private String unidadMedida;
	private int cantidadProducto;
	private int stockMinimo;
	private int stockMaximo;
	private float precioVenta;
	private float precioCompra;
	private String presentacion;
	private String descripcion;
	
	public String getCodigoBarra() {
		return codigoBarra;
	}
	public void setCodigoBarra(String codigoBarra) {
		this.codigoBarra = codigoBarra;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getMarca() {
		return marca;
	}
	public void setMarca(String marca) {
		this.marca = marca;
	}
	public String getTipo() {
		return tipo;
	}
	public void setTipo(String tipo) {
		this.tipo = tipo;
	}
	public String getContenido() {
		return contenido;
	}
	public void setContenido(String contenido) {
		this.contenido = contenido;
	}
	public String getUnidadMedida() {
		return unidadMedida;
	}
	public void setUnidadMedida(String unidadMedida) {
		this.unidadMedida = unidadMedida;
	}
	public int getCantidadProducto() {
		return cantidadProducto;
	}
	public void setCantidadProducto(int cantidadProducto) {
		this.cantidadProducto = cantidadProducto;
	}
	public int getStockMinimo() {
		return stockMinimo;
	}
	public void setStockMinimo(int stockMinimo) {
		this.stockMinimo = stockMinimo;
	}
	public int getStockMaximo() {
		return stockMaximo;
	}
	public void setStockMaximo(int stockMaximo) {
		this.stockMaximo = stockMaximo;
	}
	public float getPrecioVenta() {
		return precioVenta;
	}
	public void setPrecioVenta(float precioVenta) {
		this.precioVenta = precioVenta;
	}
	public float getPrecioCompra() {
		return precioCompra;
	}
	public void setPrecioCompra(float precioCompra) {
		this.precioCompra = precioCompra;
	}
	public String getPresentacion() {
		return presentacion;
	}
	public void setPresentacion(String presentacion) {
		this.presentacion = presentacion;
	}
	public String getDescripcion() {
		return descripcion;
	}
	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}
	@Override
	public String toString() {
		return "Producto [codigoBarra=" + codigoBarra + ", nombre=" + nombre + ", marca=" + marca + ", tipo=" + tipo
				+ ", contenido=" + contenido + ", unidadMedida=" + unidadMedida + ", cantidadProducto="
				+ cantidadProducto + ", stockMinimo=" + stockMinimo + ", stockMaximo=" + stockMaximo + ", precioVenta="
				+ precioVenta + ", precioCompra=" + precioCompra + ", presentacion=" + presentacion + ", descripcion="
				+ descripcion + "]";
	}
	
	@Override
	public int compareTo(Producto producto) {
		return nombre.compareTo(producto.getNombre());
	}
}

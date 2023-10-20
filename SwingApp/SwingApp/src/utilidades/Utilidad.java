package utilidades;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;

public class Utilidad {

	public static void main(String[] args) {
		getProperties();

	}
	
	public static Properties getProperties(){
        Properties properties= new Properties();
        try {
            properties.load(new FileInputStream(new File("recursos/configuraciones/configuracion.properties")));
//            System.out.println(properties.get("DRIVER"));
//            System.out.println(properties.get("BASE_DATOS"));
//            System.out.println(properties.get("USUARIO"));
//            System.out.println(properties.get("CLAVE"));
//            System.out.println(properties.get("PROTOCOLO"));
            return properties;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

}

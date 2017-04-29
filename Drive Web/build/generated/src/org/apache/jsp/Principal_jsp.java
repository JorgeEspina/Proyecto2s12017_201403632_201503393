package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import java.lang.String;
import Clases.Datos;

public final class Principal_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html>\n");
      out.write("    <head>\n");
      out.write("        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n");
      out.write("        <title>Principal</title>\n");
      out.write("        <meta charset=\"utf-8\" />\n");
      out.write("        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n");
      out.write("        <!--[if lte IE 8]><script src=\"assets/js/ie/html5shiv.js\"></script><![endif]-->\n");
      out.write("        <link rel=\"stylesheet\" href=\"assets/css/main.css\" />\n");
      out.write("        <!--[if lte IE 8]><link rel=\"stylesheet\" href=\"assets/css/ie8.css\" /><![endif]-->\n");
      out.write("    </head>\n");
      out.write("    <body>\n");
      out.write("        <!-- Header -->\n");
      out.write("        <section id=\"header\">\n");
      out.write("            <header>\n");
      out.write("                <span class=\"image avatar\"><img src=\"images/pro.jpg\" alt=\"\" /></span>\n");
      out.write("                <h1 id=\"logo\"><a href=\"#\">  ");
      out.print((String) session.getAttribute( "theName" ) );
      out.write(" </a></h1>\n");
      out.write("                <p>Bienvenido a la aplicacion Drive de Creacion de carpetas <br />\n");
      out.write("                    y modificacion, Eliminacion,Carga,Descarga de Archivos</p>\n");
      out.write("            </header>\n");
      out.write("            <nav id=\"nav\">\n");
      out.write("                <ul>\n");
      out.write("                    <li><a href=\"#one\" class=\"active\">Menu</a></li>\n");
      out.write("                  \n");
      out.write("                    <li><a href=\"#four\">About</a></li>\n");
      out.write("                </ul>\n");
      out.write("            </nav>\n");
      out.write("            <footer>\n");
      out.write("                <ul class=\"icons\">\n");
      out.write("                    <li><a href=\"#\" class=\"icon fa-twitter\"><span class=\"label\">Twitter</span></a></li>\n");
      out.write("                    <li><a href=\"#\" class=\"icon fa-facebook\"><span class=\"label\">Facebook</span></a></li>\n");
      out.write("                    <li><a href=\"#\" class=\"icon fa-instagram\"><span class=\"label\">Instagram</span></a></li>\n");
      out.write("                    <li><a href=\"#\" class=\"icon fa-github\"><span class=\"label\">Github</span></a></li>\n");
      out.write("                    <li><a href=\"#\" class=\"icon fa-envelope\"><span class=\"label\">Email</span></a></li>\n");
      out.write("                </ul>\n");
      out.write("            </footer>\n");
      out.write("        </section>\n");
      out.write("\n");
      out.write("        <!-- Wrapper -->\n");
      out.write("        <div id=\"wrapper\">\n");
      out.write("\n");
      out.write("            <!-- Menu -->\n");
      out.write("            <div id=\"main\">\n");
      out.write("\n");
      out.write("                <!-- One -->\n");
      out.write("                <section id=\"one\">\n");
      out.write("                    <div class=\"container\">\n");
      out.write("                        <header class=\"major\">\n");
      out.write("                            <h2>Drive</h2>\n");
      out.write("                            <p>Ingreso de Activos de Renta</p>\n");
      out.write("                            <form method=\"post\" action=\"#\">\n");
      out.write("                                <div class=\"row uniform\">\n");
      out.write("                                    <div class=\"12u\"><input type=\"text\" name=\"nombre\" id=\"name\" placeholder=\"Nombre\" /></div>\n");
      out.write("                                </div>\n");
      out.write("                               \n");
      out.write("                                <div class=\"row uniform\">\n");
      out.write("                                    <div class=\"12u\">\n");
      out.write("                                        <ul class=\"actions\">\n");
      out.write("                                            <li><input type=\"submit\" class=\"special\" value=\"Crear Carpeta\" /></li>\n");
      out.write("                                                ");

                                                    try {

                                                        if (request.getParameter("nombre") != null) {
                                                            Datos d = new Datos();
                                                            d.setNombreProducto(request.getParameter("nombre"));
                                                            d.setDescripcion(request.getParameter("descripcion"));
                                                             //= "andre";//d.getUsuario();
                                                                                                           
                                                    
                                                           // d.CreacionActivos(Usu, NomP, Desc, Empre, Dep);
                                                            /*out.println("<br>Tu Usuario es: " + d.getUsuario());
                                                            out.println("<br>Tu Contraseña es: " + d.getContraseña());
                                                            out.println("<br>Tu Empresa es: " + d.getEmpresa());
                                                            out.println("<br>Tu Departamento es: " + d.getDepartamento());
                                                            out.println("<br>Tu Nombre es: " + d.getNombre());*/
                                                        }
                                                    } catch (Exception ex) {
                                                        out.println("");
                                                    }
                                             
      out.write("\n");
      out.write("                                            <li><input type=\"text\" class=\"special\" value=\"Eliminar Carpeta\" /></li>\n");
      out.write("                                             ");

                                                    try {

                                                        if (request.getParameter("nombre") != null) {
                                                            Datos d = new Datos();
                                                            d.setNombreProducto(request.getParameter("nombre"));
                                                            d.setDescripcion(request.getParameter("descripcion"));
                                                             //= "andre";//d.getUsuario();
                                                                                                           
                                                    
                                                           // d.CreacionActivos(Usu, NomP, Desc, Empre, Dep);
                                                            /*out.println("<br>Tu Usuario es: " + d.getUsuario());
                                                            out.println("<br>Tu Contraseña es: " + d.getContraseña());
                                                            out.println("<br>Tu Empresa es: " + d.getEmpresa());
                                                            out.println("<br>Tu Departamento es: " + d.getDepartamento());
                                                            out.println("<br>Tu Nombre es: " + d.getNombre());*/
                                                        }
                                                    } catch (Exception ex) {
                                                        out.println("");
                                                    }
                                             
      out.write("\n");
      out.write("                                            <li><input t\n");
      out.write("                                            <li><input type=\"submit\" class=\"special\" value=\"Modificar Carpeta\" /></li>\n");
      out.write("                                            <li><input type=\"submit\" class=\"special\" value=\"Cargar Archivos\" /></li>\n");
      out.write("                                            <li><input type=\"submit\" class=\"special\" value=\"Descargar Archivos\" /></li>\n");
      out.write("                                            <li><input type=\"submit\" class=\"special\" value=\"Compartir Archivos\" /></li>\n");
      out.write("\n");
      out.write("                                        </ul>\n");
      out.write("                                    </div>\n");
      out.write("                                </div>\n");
      out.write("                            </form>\n");
      out.write("                        </header>\n");
      out.write("                        <p></p>\n");
      out.write("                    </div>\n");
      out.write("                </section>\n");
      out.write("\n");
      out.write("               \n");
      out.write("\n");
      out.write("                <!-- Four -->\n");
      out.write("                <section id=\"four\">\n");
      out.write("                    <div class=\"container\">\n");
      out.write("                        <header class=\"major\">\n");
      out.write("                            <h3>About</h2>\n");
      out.write("                                <p>Estructuras de Datos</p>\n");
      out.write("                                <span class=\"image avatar\"><img src=\"images/pro.jpg\" alt=\"\" /></span>\n");
      out.write("                        </header>\n");
      out.write("                    </div>\n");
      out.write("                </section>\n");
      out.write("\n");
      out.write("\n");
      out.write("            </div>\n");
      out.write("\n");
      out.write("            <!-- Footer -->\n");
      out.write("            <section id=\"footer\">\n");
      out.write("                <div class=\"container\">\n");
      out.write("                    <ul class=\"copyright\">\n");
      out.write("                        <li>&copy; Untitled. All rights reserved.</li><li>Design: <a href=\"http://html5up.net\">HTML5 UP</a></li>\n");
      out.write("                    </ul>\n");
      out.write("                </div>\n");
      out.write("            </section>\n");
      out.write("\n");
      out.write("        </div>\n");
      out.write("\n");
      out.write("        <!-- Scripts -->\n");
      out.write("        <script src=\"assets/js/jquery.min.js\"></script>\n");
      out.write("        <script src=\"assets/js/jquery.scrollzer.min.js\"></script>\n");
      out.write("        <script src=\"assets/js/jquery.scrolly.min.js\"></script>\n");
      out.write("        <script src=\"assets/js/skel.min.js\"></script>\n");
      out.write("        <script src=\"assets/js/util.js\"></script>\n");
      out.write("        <!--[if lte IE 8]><script src=\"assets/js/ie/respond.min.js\"></script><![endif]-->\n");
      out.write("        <script src=\"assets/js/main.js\"></script>\n");
      out.write("\n");
      out.write("    </body>\n");
      out.write("</html>\n");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}

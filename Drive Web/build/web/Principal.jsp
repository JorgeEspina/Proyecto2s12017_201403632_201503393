<%-- 
    Document   : Principal
    Created on : 28-abr-2017, 23:39:18
    Author     : Jorge Espina
--%>

<%@page import="java.lang.String"%>
<%@page import="Clases.Datos"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Principal</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
        <link rel="stylesheet" href="assets/css/main.css" />
        <!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->
    </head>
    <body>
        <!-- Header -->
        <section id="header">
            <header>
                <span class="image avatar"><img src="images/pro.jpg" alt="" /></span>
                <h1 id="logo"><a href="#">  <%=(String) session.getAttribute( "theName" ) %> </a></h1>
                <p>Bienvenido a la aplicacion Drive de Creacion de carpetas <br />
                    y modificacion, Eliminacion,Carga,Descarga de Archivos</p>
            </header>
            <nav id="nav">
                <ul>
                    <li><a href="#one" class="active">Menu</a></li>
                  
                    <li><a href="#four">About</a></li>
                </ul>
            </nav>
            <footer>
                <ul class="icons">
                    <li><a href="#" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
                    <li><a href="#" class="icon fa-facebook"><span class="label">Facebook</span></a></li>
                    <li><a href="#" class="icon fa-instagram"><span class="label">Instagram</span></a></li>
                    <li><a href="#" class="icon fa-github"><span class="label">Github</span></a></li>
                    <li><a href="#" class="icon fa-envelope"><span class="label">Email</span></a></li>
                </ul>
            </footer>
        </section>

        <!-- Wrapper -->
        <div id="wrapper">

            <!-- Menu -->
            <div id="main">

                <!-- One -->
                <section id="one">
                    <div class="container">
                        <header class="major">
                            <h2>Drive</h2>
                            <p>Direccion de Archivo o Carpeta a Crear</p>
                            <form method="post" action="#">
                                <div class="row uniform">
                                    <div class="12u"><input type="text" name="nombre" id="name" placeholder="Direccion Carpeta" /></div>
                                </div>
                               
                                <div class="row uniform">
                                    <div class="12u">
                                        <ul class="actions">
                                            <li><input type="submit" class="special" value="Crear Carpeta" /></li>
                                                <%
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
                                             %>
                                            <li><input type="reset" class="special" value="Eliminar Carpeta" /></li>
                                          
                                            <li><input type="Button" class="special" value="Modificar Carpeta" /></li>
                                            <li><input type="submit" class="special" value="Cargar Archivos" /></li>
                                            <li><input type="submit" class="special" value="Descargar Archivos" /></li>
                                            <li><input type="submit" class="special" value="Compartir Archivos" /></li>

                                        </ul>
                                    </div>
                                </div>
                            </form>
                        </header>
                        <p></p>
                    </div>
                </section>

               

                <!-- Four -->
                <section id="four">
                    <div class="container">
                        <header class="major">
                            <h3>About</h2>
                                <p>Estructuras de Datos</p>
                                <span class="image avatar"><img src="images/pro.jpg" alt="" /></span>
                        </header>
                    </div>
                </section>


            </div>

            <!-- Footer -->
            <section id="footer">
                <div class="container">
                    <ul class="copyright">
                        <li>&copy; Untitled. All rights reserved.</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
                    </ul>
                </div>
            </section>

        </div>

        <!-- Scripts -->
        <script src="assets/js/jquery.min.js"></script>
        <script src="assets/js/jquery.scrollzer.min.js"></script>
        <script src="assets/js/jquery.scrolly.min.js"></script>
        <script src="assets/js/skel.min.js"></script>
        <script src="assets/js/util.js"></script>
        <!--[if lte IE 8]><script src="assets/js/ie/respond.min.js"></script><![endif]-->
        <script src="assets/js/main.js"></script>

    </body>
</html>

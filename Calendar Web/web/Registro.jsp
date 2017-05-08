<%-- 
    Document   : Registro
    Created on : 28-abr-2017, 23:08:24
    Author     : Jorge Espina
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Registro</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="css/style.css" type="text/css" media="all" /> <!-- Style-CSS --> 
        <link rel="stylesheet" href="css/font-awesome.css"> <!-- Font-Awesome-Icons-CSS -->
        <link href="//fonts.googleapis.com/css?family=Josefin+Sans:100,100i,300,300i,400,400i,600,600i,700,700i&amp;subset=latin-ext" rel="stylesheet">
        <%@ page  import="Clases.Datos" errorPage=""%>

    </head>
    <body>
        <!--header-->
        <div class="header-w3l">
            <h1>Calendar</h1>
        </div>
        
        <!--//header-->

        <!--main-->
        <div class="main-content-agile">
            <div class="sub-main-w3">	
                <div class="wthree-pro">
                    <img src="images/pro.jpg" alt="image">
                    <h2>Registro de Drive</h2>
                </div>
                <form action="#" method="post">
                    <input placeholder="Nombre de Usuario" name="Name" class="user" type="text" required="" >
                    <input placeholder="Nombre " name="Nombre" class="nomb" type="text" required="" >
                    <input  placeholder="Password" name="Password" class="pass" type="password" required="">                   
                   
                    <div class="12u">
                        <input type="submit" id="Crear Usuario">
                        <%
                            try {

                                if (request.getParameter("Name") != null) {
                                    Datos d = new Datos();
                                  d.setUsuario(request.getParameter("Name"));
                                    d.setContraseña(request.getParameter("Password"));
                                    d.setNombre(request.getParameter("Nombre"));
                                    String Usu = d.getUsuario();
                                    String Con = d.getContraseña();                                    
                                    String Nom = d.getNombre();
                                    //d.Registrarse(Usu,Con,Nom,Dep,Empre);
                                   /* out.println("<br>Tu Usuario es: " + d.getUsuario());
                                    out.println("<br>Tu Contraseña es: " + d.getContraseña());
                                    out.println("<br>Tu Empresa es: " + d.getEmpresa());
                                    out.println("<br>Tu Departamento es: " + d.getDepartamento());
                                    out.println("<br>Tu Nombre es: " + d.getNombre());*/
                                }
                            } catch (Exception ex) {
                                out.println("");
                            }
                        %>
                    </div>
                            <div class="top-big-link">
                                <a class="btn btn-link-3" href="index.jsp">Inicio</a>
                            </div>
                </form>
            </div>
        </div>
    </body>
</html>

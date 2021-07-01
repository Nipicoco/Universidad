<?php
/* CONECTAR CON BASE DE DATOS **************** */
$servername = "localhost";
$username = "root";
$password = "";
$BD="ejemplo1";

$con = new mysqli($servername, $username, $password, $BD);

// Check connection
if ($con->connect_error) {
    die("Connection failed: " . $con->connect_error);
}
//echo "Connected successfully";

/* ********************************************** */
$nombre=$_POST['Nombre'];
$ap_paterno=$_POST['Paterno'];
$ap_materno=$_POST['Materno'];
$sexo=$_POST['sexo'];
//REALIZAR CONSULTA
$sql = "INSERT INTO DATOS (id, nombre, ap_paterno, ap_materno, sexo) VALUES ('0','$nombre','$ap_paterno', '$ap_materno', '$sexo')";

if ($con->query($sql) === TRUE) {
    ob_start();
      header("refresh: 3; url = index.html");
      echo 'Datos insertados correctamente, Espere un momento y será redireccionado...';
    ob_end_flush();
} else {
    echo "Error: " . $sql . "<br>" . $con->error;
}

$con->close();
?>
<h1>Lista de los primeros 100 emleados</h1>
<a href="./">Volver al inicio</a> <br/><br/>

<?php 
require './config/db.php';

$sql = "CALL obtener_empleados()";
$resultado = $mysqli->query($sql);

if($resultado->num_rows > 0){
    echo 'Si, existen empleados. Cantidad: '.$resultado->num_rows;
}else{
    echo 'No, no existen empleados';
}
echo '<br/><br/><br/><br/>';

while ($row = $resultado->fetch_assoc()) {
   echo 'ID: '.$row['emp_no'].' | Nombre: '.$row['first_name'].' | Apellido: '.$row['last_name'].'<br/>';
}

?>
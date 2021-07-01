<?php

$mysqli = new mysqli("localhost", "root", "", "employees");
if ($mysqli->connect_errno) {
    echo "Fallo al conectar a MySQL:";
}
$mysqli->set_charset("utf8");

?>

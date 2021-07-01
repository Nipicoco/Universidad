<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Formulario para insertar empleado </title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
</head>
<body>
    <h1>Formulario para insertar empleado</h1>
    <a href="./">Volver al inicio</a> <br/><br/>
    <form action='./obtiene_e_instarta_empleado.php' method='post'>
        <input type="number" placeholder="Numero de empleado" name="emp_no" required/> <br/><br/>
        <input type="text" placeholder="Nombre del empleado" name="first_name" required/> <br/><br/>
        <input type="text" placeholder="Apellido del empleado" name="last_name" required/> <br/><br/>
        <input type="date" placeholder="Fecha de nacimiento" name="birth_date" required/> <br/><br/>
        <input type="date" placeholder="Fecha de contratación" name="hire_date" required/> <br/><br/>
        <select name="gender">
            <option value="M">Masculino</option>
            <option value="F">Femenino</option>
        </select>
        <br/><br/>
        <button type="submit">Insertar empleado</button>
    </form>
</body>
</html>
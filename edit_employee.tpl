% include('header.tpl')
		<h2>MySQL + Python (Bottle)</h2>
		<p>Edit the task with ID = {{no}}</p>
    <p>Actualiza los datos del empleado</p>
    <form action="/save" method="POST">
			<input type="hidden" name="mode" value="update" />
			<input type="hidden" name="Id" value="{{row[0]}}" />
			<label>Nombres:
				<input type="text" name="Names" value="{{row[1]}}" />
			</label>
			<label>Dirección:
				<input type="text" name="Address" value="{{row[2]}}" />
			</label>
			<label>Fecha registro
				<input type="date" name="Date_register" value="{{row[3]}}" />
			</label>
			<label>Telefono
				<input type="tel" name="Phone" value="{{row[4]}}" />
			</label>
			<label>Comentario
				<textarea name="Comment">{{row[5]}}</textarea>
			</label>
			<label>Salario
				<input type="number" step=".01" name="Salary" value="{{row[6]}}" />
			</label>
			<button type="submit" value="Save">Enviar datos</button>
		</form>
		<p><a href="/list">Regresar a listado</a></p>
% include('footer.tpl')

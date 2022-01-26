% include('header.tpl')
		<h2>MySQL + Python (Bottle)</h2>
    <p>Registra los datos del nuevo empleado</p>
    <form action="/save" method="POST">
			<input type="hidden" name="mode" value="new" />
			<input type="hidden" name="Id" value="0" />
			<label>Nombres:
				<input type="text" name="Names" />
			</label>
			<label>Dirección:
				<input type="text" name="Address" />
			</label>
			<label>Fecha registro
				<input type="date" name="Date_register" />
			</label>
			<label>Telefono
				<input type="tel" name="Phone" />
			</label>
			<label>Comentario
				<textarea name="Comment"></textarea>
			</label>
			<label>Salario
				<input type="number" step=".01" name="Salary" />
			</label>
			<button type="submit" value="Save">Enviar datos</button>
		</form>
		<p><a href="/list">Regresar a listado</a></p>
% include('footer.tpl')

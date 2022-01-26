% include('header.tpl')
		<h2>MySQL + Python (Bottle)</h2>
    <p>La consulta arrojo lo siguiente resultados:</p>
    <table class="listEmployees" border="1">
    %for row in rows:
      <tr>
      %for col in row:
        <td>{{col}}</td>
      %end
		<td><a href="/edit/{{row[0]}}">Edit</a></td>
		<td><a data-id="{{row[0]}}" class="del" href="#">Eliminar</a></td>
      </tr>
    %end
    </table>
		<p><a href="/new">Añadir nuevo empleado</a></p>
% include('footer.tpl')

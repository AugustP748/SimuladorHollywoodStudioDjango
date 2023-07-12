
document.getElementById('btnSimular').addEventListener('click', function() {
  // Realizar una solicitud AJAX al servidor para obtener los datos
  fetch('./templates/home.html')
    .then(response => response.json())
    .then(data => {
      // Manipular los datos recibidos
      // Por ejemplo, puedes actualizar la tabla con los nuevos datos
      actualizarTabla(data);
    })
    .catch(error => {
      console.error('Error al obtener los datos:', error);
    });
});

function actualizarTabla(data) {
  // Actualizar la tabla con los datos recibidos
  // Por ejemplo, puedes iterar sobre los datos y construir las filas de la tabla
  var tableBody = document.getElementById('tablaBody');
  tableBody.innerHTML = '';

  data.forEach(function(row) {
    var newRow = document.createElement('tr');
    newRow.innerHTML = '<td>' + row.hora + '</td><td>' + row.RR + '</td><td>' + row.MF + '</td>';
    tableBody.appendChild(newRow);
  });
}


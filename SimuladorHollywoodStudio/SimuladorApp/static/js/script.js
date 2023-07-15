
const getDataTable = async () => {
  try{
    const response = await fetch('./table-data');
    const data = await response.json();  
    console.log(data);
  } catch(e){
    console.log(e);
  }
};

document.getElementById('simular-btn').addEventListener('click', function() {
   getDataTable();
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


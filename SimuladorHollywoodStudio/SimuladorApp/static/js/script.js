function actualizarTabla(data) {
  // Actualizar la tabla con los datos recibidos
  // Por ejemplo, puedes iterar sobre los datos y construir las filas de la tabla
  var tableBody = document.getElementById('tablaBody');
  
  console.log(data);

  data.table_data.forEach(function(row) {
    console.log(row.hora);

    const tr = document.createElement("tr");

    const tdhora = document.createElement("td");
    let txthora = document.createTextNode(row.hora);
    tdhora.appendChild(txthora);
    txthora.className = "hora";
    
    const tdRR = document.createElement("td");
    let txtRR = document.createTextNode(row.RR);
    tdRR.appendChild(txtRR);
    txtRR.className = "RR";

    const tdMF = document.createElement("td");
    let txtMF = document.createTextNode(row.MF);
    tdMF.appendChild(txtMF);
    txtMF.className = "MF";

    tr.appendChild(tdhora);
    tr.appendChild(tdRR);
    tr.appendChild(tdMF);

    
    tablaBody.appendChild(tr);

  });
}

const getDataTable = async () => {
  try{
    const response = await fetch('./table-data');
    const data = await response.json(); 
    actualizarTabla(data); 
    console.log(data);
  } catch(e){
    console.log(e);
  }
};

document.getElementById('simular-btn').addEventListener('click', function() {
   getDataTable();
});



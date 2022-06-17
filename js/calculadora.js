let inputNombre = document.querySelector('#inputNombre');
let inputMonto = document.querySelector('#inputMonto');
let contenedorMontoTotal = document.querySelector('#contenedorMontoTotal');
let contenedorDivGastos = document.querySelector('#contenedorDivGastos');

let escribirHeader = true;

contenedorDivGastos.innerHTML = '<strong>Aporte individual:</strong> $0';
contenedorMontoTotal.innerHTML = '<strong>Total:</strong> $0';

//Estructura base de la tabla
let tabla = document.querySelector('#table');
let thead = document.createElement('thead');
let tbody = document.createElement('tbody');
tabla.appendChild(thead);
tabla.appendChild(tbody);

let nombres = [];
let montos = [];

inicializarTabla();

function agregar(){
    let tamanio = nombres.length;
    let nombre = inputNombre.value;
    nombre = nombre.replace(/\w\S*/g, (w) => (w.replace(/^\w/, (c) => c.toUpperCase()))); //Pone la primera letra en mayuscula. Obtenido de google.
    let monto = +inputMonto.value;
    if(nombre != '' && monto != ''){
        for(let i = 0; i < tamanio; i++){
            if(nombre == nombres[i]){
                montos[i] += monto;
                tabla.rows[i+1].cells[1].innerHTML = montos[i];
                inputNombre.value = '';
                inputMonto.value = '';
                return true;
            }
        }
        nombres.push(nombre);
        montos.push(monto);
        inputNombre.value = '';
        inputMonto.value = '';
        return true;
    }
    return false;
}

function calculoTotal(){
    let total = 0;
    let tamanio = montos.length;
    for(let i = 0; i < tamanio; i++){
        total += +montos[i];
    }
    contenedorMontoTotal.innerHTML = `<strong>Total:</strong> $${total}`;
    return total;
}

function calculoGastos(total){
    let tamanio = montos.length;
    let gastoInd = (total/tamanio).toFixed(2);
    contenedorDivGastos.innerHTML = `<strong>Aporte individual:</strong> $${gastoInd}`;
    return gastoInd;
}

function compensarGastos(gastoInd){
    let tamanio = nombres.length;
    let saldo = 0;
    let saldos = [];
    for (let i = 0; i < tamanio; i++){
        saldo = (gastoInd - montos[i]).toFixed(2);
        saldos.push(saldo);
    }
    return saldos;
}

function crearTabla(nombres, montos, saldos){
    let tamanio = nombres.length;
    if(tabla.rows.length - 1 < tamanio){
        let fila = document.createElement('tr');
        let columna1 = document.createElement('td');
        let columna2 = document.createElement('td');
        let columna3 = document.createElement('td');
        let columna4 = document.createElement('td');
        columna1.innerHTML = nombres[tamanio-1];
        columna2.innerHTML = montos[tamanio-1];
        fila.appendChild(columna1);
        fila.appendChild(columna2);
        fila.appendChild(columna3);
        fila.appendChild(columna4);
        tbody.appendChild(fila);
    }
    for (let i = 0; i < tamanio; i++){
        if (saldos[i] == 0){
            tabla.rows[i + 1].cells[2].innerHTML = "";
            tabla.rows[i + 1].cells[3].innerHTML = "";
        } else if(saldos[i] < 0){
            tabla.rows[i + 1].cells[3].innerHTML = Math.abs(saldos[i]);
            tabla.rows[i + 1].cells[2].innerHTML = "";
        } else if(saldos[i] > 0){
            tabla.rows[i + 1].cells[2].innerHTML = Math.abs(saldos[i]);
            tabla.rows[i + 1].cells[3].innerHTML = "";
        }
    }
}

function inicializarTabla(){
    let filaHeader = document.createElement('tr');
    filaHeader.className = 'tablaHeader';
    let header1 = document.createElement('th');
    header1.innerHTML = 'Nombre';
    let header2 = document.createElement('th');
    header2.innerHTML = 'Monto';
    let header3 = document.createElement('th');
    header3.innerHTML = 'Compensa con';
    let header4 = document.createElement('th');
    header4.innerHTML = 'Recibe';
    filaHeader.appendChild(header1);
    filaHeader.appendChild(header2);
    filaHeader.appendChild(header3);
    filaHeader.appendChild(header4);
    thead.appendChild(filaHeader);
}

function calculo() {
    if (!agregar()){
        return
    }
    let total = calculoTotal();
    let gastoInd = calculoGastos(total);
    let saldos = compensarGastos(gastoInd);
    crearTabla(nombres, montos, saldos);
    console.log(tabla.rows.length);

}

document.querySelector('.calculadora').style.display = 'none';
function mostrarCalculadora(){
    if (document.querySelector('.calculadora').style.display == 'none'){
        document.querySelector('.calculadora').style.display = 'flex';
        document.querySelector('.seccion').style.filter = 'blur(5px)';
    }else{
        document.querySelector('.calculadora').style.display = 'none';
        document.querySelector('.seccion').style.filter = 'none';
    }
}

function reset(){
    while (tbody.firstChild) {
        tbody.removeChild(tbody.firstChild);
    }
    contenedorDivGastos.innerHTML = '<strong>Aporte individual:</strong> $0';
    contenedorMontoTotal.innerHTML = '<strong>Total:</strong> $0';
    inputNombre.value = '';
    inputMonto.value = '';
    nombres = [];
    montos = [];
}

function borradoInputs(){
    inputNombre.value = '';
    inputMonto.value = '';
}
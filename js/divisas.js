const url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales";
const divisas = new Set([
    "Dolar Oficial",
    "Dolar Blue",
    "Dolar Contado con Liqui",
    "Dolar Bolsa",
    "Dolar turista",
    "Dolar",
]);
const divDivisas = document.getElementById("divisas");

const date = new Date();
const actualDate =
    date.getFullYear() +
    "-" +
    String(date.getMonth() + 1).padStart(2, "0") +
    "-" +
    String(date.getDate()).padStart(2, "0");

function mostrarDivisa(divisa) {
    divDivisas.innerHTML += 
    `<div class="col-12 col-md-6 col-lg-2 mb-2 mt-2 my-lg-2">
        <article class="card h-100 me-2 me-lg-0 bg-secondary shadow"> 
            <div class="card-body rounded">
                <div class="venta-compra">
                    <div class="d-flex justify-content-center w-100 align-items-center mb-2 gap-2">
                        <div class="contenedor-img-dolar">
                            <img class="w-100 h-100" src="img/dolar.png" alt="Ícono Dolar">
                        </div>
                        <h5 class="card-title text-center m-0 fs-6">${divisa.nombre}</h5>
                    </div>
                        <p class="card-text">Venta: $${divisa.venta} <br>
                    Compra: $${divisa.compra}</p>
                </div>
                <div>
                    <p class="card-text my-2 variacion${divisa.variacion < 0 ? "-negativa" : divisa.variacion > 0 ? "-positiva" : ""}">
                        Variación: ${String(divisa.variacion).replace(".", ",")}%
                    </p>
                    <p class="card-text">
                        Fecha de actualización: ${actualDate}
                    </p>
                    <div>
                </div>
            </div>
        </article>
    </div>`;
}

fetch(url)
    .then((response) => response.json())
    .then((data) => {
        filteredData = data.reduce((arr, item) => {
            if (divisas.has(item.casa.nombre)) {
                if (item.casa.nombre == "Dolar") {
                    item.casa.variacion = arr[0].variacion;
                    item.casa.nombre = "Dolar Promedio";
                }
                if (item.casa.nombre == "Dolar Contado con Liqui") item.casa.nombre = "Contado Liqui";
                item.casa.variacion = parseFloat(
                    item.casa.variacion.replace(",", ".")
                ).toFixed(2);
                return [...arr, item.casa];
            }
            return arr;
        }, []);

        filteredData.forEach(mostrarDivisa);
    });

<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-sm-6 text-center">

          <div class="row"><h1>Usuario 1</h1></div>

          <div class="row container-btn">
            <div class="col-sm-6 text-center">
              <button type="button" class="btn btn-primary">Acusar</button>
            </div>

            <div class="col-sm-6 text-center">
                <button type="button" class="btn btn-secondary">Preguntar</button>
            </div>
          </div>

          <div class="row cart-container">
            <div class="col-sm-3 cart">a</div>
            <div class="col-sm-3 cart">b</div>
            <div class="col-sm-3 cart">c</div>
            <div class="col-sm-3 cart">d</div>
          </div>
        </div>
        <div class="col-sm-6 text-center">
          <table class="table table-hover">
            <thead class="table-dark">
              <tr>
                <th scope="col">#</th>
                <th scope="col">Quien</th>
                <th scope="col">Notas</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">1</th>
                <td>Pedro</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">2</th>
                <td>Juan</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">3</th>
                <td>Carlos</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">4</th>
                <td>Juanita</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">5</th>
                <td>Antonio</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">6</th>
                <td>Carolina</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">7</th>
                <td>Manuel</td>
                <td></td>
              </tr>
              <tr class="table-dark">
                <th scope="col">8</th>
                <td>Modulo</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">9</th>
                <td>Nomina</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">10</th>
                <td>Facturación</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">11</th>
                <td>Recibos</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">12</th>
                <td>Comprobante contable</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">13</th>
                <td>Usuarios</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">14</th>
                <td>Contabilidad</td>
                <td></td>
              </tr>
              <tr class="table-dark">
                <th scope="col">15</th>
                <td scope="col">Tipo de error</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">16</th>
                <td>404</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">17</th>
                <td>Stack overflow</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">18</th>
                <td>Memory out of range</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">19</th>
                <td>Null pointer</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">20</th>
                <td>Syntax error</td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">21</th>
                <td>Encoding error</td>
                <td></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>



</template>

<script>
export default {
  name: "Game",
};
</script>

<style>
.cart-container{
  position: fixed;
  bottom: 20px;
  border: 1px solid lightgray;
  padding: 20px;
  width: 40%;
}

.cart{
  border-right: 1px solid lightgray;
}

.container-btn{
  width: 40%;
  position: fixed;
  top: 30%;
}
</style>

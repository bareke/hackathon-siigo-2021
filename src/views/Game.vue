<template>
  <div>
    <p>Component Game</p>
    <div class="container">
      <div class="row">
        <div class="col-sm-6 text-center">
          <button type="button" class="btn btn-primary">Acusar</button>
          <hr />
          <button type="button" class="btn btn-secondary">Preguntar</button>
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
</style>

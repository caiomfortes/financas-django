$(document).ready(function() {
  
  setInterval(data_atual, 1000);

  var selectUrl = getCentralUrl()
  const sideOp = document.querySelectorAll('.sidebar a');
  selectUrl = "side-" + selectUrl
  
  sideOp.forEach((item, index) => {
    if(index > 0 && selectUrl === item.id){
      sideOp.forEach(item => item.classList.remove('select-page'));
      item.classList.add('select-page');
    }
  });

  sideOp.forEach((item,index) => {
      item.addEventListener('click', () => {
        if(index>0){
          // Remove a classe 'active' de todos os itens
          sideOp.forEach(item => item.classList.remove('select-page'));
          // Adiciona a classe 'active' ao item clicado
          item.classList.add('select-page');
        }
      });
  });
  
  
  $('.sidebar a').click(function(e) {
    e.preventDefault();
    var url = $(this).data('url')
    var urlContent = $(this).data('url') + "/content";
    history.pushState({}, '', url);
    $('.content').fadeOut(400, function() {
      $.ajax({
        url: urlContent,
        success: function(data) {
          $('.content').html(data).fadeIn(400);
        }
      });
    });
  });

  
  

});

function relogio(data, texto) {
  const agora = new Date();
  const horas = agora.getHours().toString().padStart(2, '0');
  const minutos = agora.getMinutes().toString().padStart(2, '0');
  $(texto).text(data + `, às ${horas}:${minutos}`);
}

function data_atual(){
  var dataAtual = new Date();

  // Formatar a data
  var diasDaSemana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'];
  var mesesDoAno = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'];

  var diaSemana = diasDaSemana[dataAtual.getDay()];
  var diaMes = dataAtual.getDate();
  var mes = mesesDoAno[dataAtual.getMonth()];

  var dataFormatada = diaSemana + ", " + diaMes + " de " + mes;

  // Inserir a data formatada no HTML
  relogio(dataFormatada, ".content-top-wellcome p")
}


function getCentralUrl() {
  var urlCompleta = window.location.pathname;
  var partesUrl = urlCompleta.split('/');

  // Verifica se a URL tem pelo menos duas partes
  if (partesUrl.length >= 2) {
    return partesUrl[1];
  } else {
    return null; // Ou outro valor padrão
  }
}
$(document).ready(function() {
  
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
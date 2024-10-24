$(document).ready(function() {
    

    $("#button-add-mov").click(function(){
        $(".modal").show()
        $(".modal-overlay").show()
    })

    $(".modal-overlay").click(function(){
        $(".modal").hide()
        $(".modal-overlay").hide()
        limpa_modal('.modal')
    })

    $("#modal-cancelar").click(function(){
        $(".modal").hide()
        $(".modal-overlay").hide()
        limpa_modal('.modal')
    })

    
});


function limpa_modal(objeto){
    $(objeto).find('input, select, textarea').each(function() {
        // Limpa o valor de cada elemento
        $(this).val('');

        // Verifica se o elemento é um checkbox ou radio button
        if ($(this).is(':checkbox') || $(this).is(':radio')) {
            $(this).prop('checked', false);
        }

        // Limpa o conteúdo de textareas
        if ($(this).is('textarea')) {
            $(this).text('');
        }
    });
}
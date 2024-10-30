$(document).ready(function() {
    


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


    $("#button-add-mov").click(function(){
        liga_modal(".modal", ".modal-overlay")
        desliga_alerta()
    })

    $("#modal-cancelar").click(function(){
        desliga_modal(".modal", ".modal-overlay")
        $("#modal-form")[0].reset()
    })


    $('#modal-form').submit(function(event) {
        event.preventDefault();
        liga_modal_loading(".modal",".modal-save")
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            url: "/cidades",
            type: "POST",
            headers: {"X-CSRFToken": csrftoken },
            data: $("#modal-form").serialize(),
            success: function(response) {
                desliga_alerta()
                if (response.msg == "adicionado") {
                    $("#modal-form")[0].reset()
                    desliga_modal_loading(".modal-save")
                }
                else if(response.msg == "existente"){
                    alerta_modal_loading(".modal-save")
                }
            }
        });
    });

});


function mensagem_error(mensagem) {
    $(".alert-error").text(mensagem);
    $(".alert-error").show();
}


function liga_modal_loading(modal, modal_save){
    $(modal).animate({
        opacity: 0,
        marginTop: '-5%'
      }, 500, function() {
        // Função a ser executada após a animação
        $(this).hide();
        $(modal_save).show();
        $(".sidebar-overlay").show()
        $(modal_save).animate({
            opacity: 1,
            marginTop: '0'
        }, 500)
        $(".sidebar-overlay").animate({
            opacity: 1,
            marginTop: '0'
        }, 500)
    })
}


function desliga_modal_loading(modal_save){
    setTimeout(function(){
        $(modal_save + " #loading").animate({
            opacity: 0,
            marginTop: '0'
        }, 500, function() {
            // Função a ser executada após a animação
            $(modal_save + " #loading").hide(300)
            $(modal_save + " #saved").show(300)
            $(modal_save + " #saved").animate({
                opacity: 1,
                marginTop: '0'
            }, 500)
            setTimeout(function(){
                $(modal_save).animate({
                    opacity: 0,
                    marginTop: '0'
                }, 500, function(){
                    $(modal_save).hide();
                    $(modal_save + " #saved").css('opacity', 0)
                    $(modal_save + " #loading").css('opacity', 1)
                    $(modal_save + " #loading").show()
                    $(modal_save + " #saved").hide()
                    $(".modal-overlay").animate(
                        {opacity: 0,marginTop: '0'},500,
                        function(){
                            $(this).hide()
                        });
                    $(".sidebar-overlay").animate(
                        {opacity: 0,marginTop: '0'},500,
                        function(){
                            $(this).hide()
                        })
                })

            },1500)
        })
    },2000)
}


function alerta_modal_loading(modal_save){
    setTimeout(function(){
        $(modal_save + " #loading").animate({
            opacity: 0,
            marginTop: '0'
        }, 500, function() {
            // Função a ser executada após a animação
            $(modal_save + " #loading").hide(300)
            $(modal_save + " #error").show(300)
            $(modal_save + " #error").animate({
                opacity: 1,
                marginTop: '0'
            }, 500)
            setTimeout(function(){
                $(modal_save).animate({
                    opacity: 0,
                    marginTop: '0'
                }, 500, function(){
                    $(modal_save).hide();
                    $(modal_save + " #error").css('opacity', 0)
                    $(modal_save + " #loading").css('opacity', 1)
                    $(modal_save + " #loading").show()
                    $(modal_save + " #error").hide()
                    $(".sidebar-overlay").animate(
                        {opacity: 0,marginTop: '0'},500,
                        function(){
                            $(this).hide()
                        })
                })
                mensagem_error("Já existe uma cidade com este nome.")
                $(".modal").show()
                $(".modal").animate({
                    opacity: 1,
                    marginTop: '5%'
                }, 500)
            },1500)
        })
    },1000)
}

function desliga_alerta(){
    $(".alert-error").text("");
    $(".alert-error").hide();
}



function liga_modal(modal,overlay){
    $(modal).show()
    $(overlay).show()
    $(modal).animate(
        {opacity: 1,marginTop: '5%'}, 500
    );
    $(overlay).animate(
        {opacity: 1,marginTop: '0'}, 500
    );
}



function desliga_modal(modal,overlay){
    $(modal).animate({
        opacity: 0,
        marginTop: '-5%'
      }, 500, function() {
        // Função a ser executada após a animação
        $(this).css('display', 'none');
    });
    $(overlay).animate({
        opacity: 0,
        marginTop: '0'
      }, 500, function() {
        // Função a ser executada após a animação
        $(this).css('display', 'none');
    });
}
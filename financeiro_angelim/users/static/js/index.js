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


  
    $('.form-1').submit(function(event) {
        event.preventDefault();
        const csrftoken = getCookie('csrftoken');
        $.ajax({
            url: "/index",
            type: "POST",
            headers: {"X-CSRFToken": csrftoken },
            data: $(".form-1").serialize(),
            success: function(response) {
                if (response.msg == "sucesso") {
                    window.location.href = 'home'
                }
            }
        });
    });



});
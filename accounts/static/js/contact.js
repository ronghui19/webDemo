const form = document.getElementById('form');
form.addEventListener('submit', submitHandler);

function submitHandler(e) {
    e.preventDefault();
    $.ajax({
        type: 'post',
        url: '{% url "contact" %}',
        data: $('#form').serialize(),
        dataType: 'json',
        success: successFunction
    });
}

function successFunction(msg) {
    if (msg.message === 'success') {
        alert('Success!');
        form.reset()
    }
}

$(document).ready(() => {
// captcha
    $('.js-captcha-refresh').click(function(){
        $form = $(this).parents('form');

        $.getJSON($(this).data('url'), {}, function(json) {
            $(".captcha").attr("src", result)
        });

        return false;
    });
});

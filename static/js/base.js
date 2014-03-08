$(function submitForm(){
	$('#lang_form').on('submit', function (e) {
        $.ajax({
            type: 'post',
            url: '/i18n/setlang/',
            data: $(this).serialize(),
            success: function () {
                location.reload();
            }
        });
        e.preventDefault();
    });
});

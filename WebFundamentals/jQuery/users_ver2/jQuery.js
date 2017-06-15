$(function() {
    $('form').submit(function() {
        return false
    });    
    $('#submitBtn').click (function() {
        // $('form').submit();
        $('tbody').append('<tr></tr>');
        $.each($('form').serializeArray(), function (i,field) {
            console.log($('form').serializeArray());
            $('tbody tr:last-child').append('<td>' + field.value + '</td>');
        });
        $('form').children('input').val('');
    });
});


// var array = $('form').serializeArray();


// for (var i = 0; i < array.length; i++) {
//     var element = array[i];
    
// }
// $(function() {
//     $('form').submit(function() {
//         return false
//     });    
//     $('#submitBtn').click (function() {
//         $('body').append('<div class = "box"></div>');
//         var arr = [];
//         $.each($('form').serializeArray(), function (i,field) {
//             arr.push(field.value);  
//         });
//         // console.log(arr);
//         $('div:last-child').append('<h2>' + arr[0] + '  ' + arr[1] + '</h2>');
//         $('div:last-child').append('<p>Click me for description!</p>');
//         $('div:last-child').append('<p style="display: none">' + arr[2] + '</p>');
//     });
//     $(document).on('click','div',function () {
//         $(this).children().toggle();
//     })
// });


//ver2.0
//added if statement to validate user's input

$(function() {
    $('form').submit(function() {
        return false
    });    
    $('#submitBtn').click (function() {
        var arr = [];
        $.each($('form').serializeArray(), function (i,field) {
            arr.push(field.value);  
        });
        for (var i = 0; i < arr.length; i++) {
            if (arr[i] === '') {
                console.log(arr)
                alert('Please complete the form before submitting.')
                return false
            }
        }
        $('body').append('<div class = "box"></div>');
        $('div:last-child').append('<h2>' + arr[0] + '  ' + arr[1] + '</h2>');
        $('div:last-child').append('<p>Click me for description!</p>');
        $('div:last-child').append('<p style="display: none">' + arr[2] + '</p>');
    });
    $(document).on('click','div',function () {
        $(this).children().toggle();
    })
});

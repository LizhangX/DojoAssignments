
//ver.1
$(function () {
    $('img').css("display","block");
    $('img').css("margin","0px 0px 5px 300px");
    $('img').click(function () {
        var temp = $(this).attr('src');
        $(this).attr('src', $(this).attr('data-alt-src'));
        $(this).attr("data-alt-src", temp);
        
        // var t = s;
        // s = a;
        // a = t
    });
});

//ver.2

// $(function () {
//     $('img').css("display","block");
//     $('img').css("margin","0px 0px 5px 300px");
//     $('img').toggle(function() {
//         $(this).attr('src',$(this).attr('data-alt-src'));
//     }, function () {
//         $(this).attr('src',$(this).attr('src'));
//     });
// })
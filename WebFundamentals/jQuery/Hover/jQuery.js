$(function () {
    $('img').css("display","block");
    $('img').css("margin","0px 0px 5px 300px");
    $('img').hover(function () {
        $(this).attr('temp', $(this).attr('src'));
        $(this).attr('src', $(this).attr("data-alt-src"));
    }, function () {
        $(this).attr('src',$(this).attr('temp'));
    }
    );
});



//         var temp = $(this).attr('src');
//         $(this).attr('src', $(this).attr("data-alt-src"));}, function name(params) {
            
//         }
//         $(this).click(function () {
//             $(this).attr('src', temp);
//         });
//     });
// });
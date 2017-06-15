$(function () {
    $('img').click(function() {
        var url = 'https://www.anapioficeandfire.com/api/houses/' + $(this).attr('id');
         $.get(url, function (res) {
             console.log(res);
            //  $('#box').empty();
             var names = '<h2>Name: ' + res.name + '</h2>';
             var words = '<h3>Words: ' + res.words + '</h3>';
             var title = '<p>Titles: ';
             for (var i = 0; i < res.titles.length; i++) {
                title = title + res.titles[i] + ', ';     
             }
             title = title.slice(0,-2) + '</p>';
             $('#box').html('<h1>House Details</h1>' + names+words+title);
        },
        "json"
        );
    })
   
})
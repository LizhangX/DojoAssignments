$(document).ready(function() {
    $('form').submit(function() {
        // your code here (build up your url)
        var url = 'http://api.openweathermap.org/data/2.5/weather?q=' + $('input').val() + ',us&appid=6ad5a5f015da7905001dfc4f4a25064e';
        $.get(url, function(res) {
            // your code here
            console.log(res);
            var temp = Math.floor(9/5 * (res.main.temp - 273) + 32);
            $('div').html('<p>It is ' + temp + ' degree in ' + res.name + '.</p>' );
        }, 'json');
        // don't forget to return false so the page doesn't refresh
        return false;
    });
});

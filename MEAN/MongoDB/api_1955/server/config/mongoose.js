var mongoose = require('mongoose');
var fs = require('fs');

mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/people', { useMongoClient: true });


var models_path = __dirname + '/../models';
fs.readdirSync(models_path).forEach(function(file){
    if(file.includes('.js')){
        console.log(`loading ${file}`);
        require(`${models_path}/${file}`);
    }
});
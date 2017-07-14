var mongoose = require('mongoose');
var People = mongoose.model('People');

module.exports = {
    index: function(req, res) {
        var people = People.find({}, function(err, data){
            if (err) {
                console.log(err);
            } else {
                return res.json(data);
            }
        });
    },
    new: function(req, res){
        var people = People.create({name: req.params.name}, function(err, data){
            if (err) {
                console.log(err);
            } else {
                return res.redirect('/');
            }
        });
    },
    remove: function(req, res){
        var people = People.findOneAndRemove(req.params.name, function(err, data){
            if (err) {
                console.log(err);
            } else {
                return res.redirect('/');                
            }
        });
    },
    show: function(req, res){
        var people = People.find({name: req.params.name}, function(err, data){
            if (err) {
                console.log(err);
            } else {
                return res.redirect('/');                
            }
        });
    }
};
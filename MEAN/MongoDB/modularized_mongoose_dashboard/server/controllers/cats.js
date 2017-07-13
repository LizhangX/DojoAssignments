var mongoose = require('mongoose');
var Cat = mongoose.model('Cat');

module.exports = {
    index: function(req, res) {
    var cats = Cat.find({}, function(err, messages){
        if (err) {
            console.log(err);
        } else {
            res.render('index.ejs', {messages: messages});
        }
    });
    },
    showNew:  function(req, res) {
    console.log('inside show new method');
    res.render('new.ejs');
    },
    showOne: function(req, res) {
    var cats = Cat.find({_id: req.params.id}, function(err, messages){
        if (err) {
            console.log(err);
        } else {
            console.log(messages);
            
            res.render('display.ejs', {messages: messages});
        }
    });
    },
    addnew: function(req, res) {
    var cats = Cat.create(req.body, function(err, cat){
        if (err) {
            let errors_arr = [];
            for (var key in err.errors) {
                var error = err.errors[key];
                errors_arr.push(error.message);  
            }
                console.log(errors_arr); 
        } else {
            console.log(cat);
            
        }
    });
    res.redirect('/');
    },
    showEdit: function(req, res) {
    var cats = Cat.find({_id: req.params.id}, function(err, messages){
        if (err) {
            console.log(err);
        } else {
            res.render('edit.ejs', {messages: messages});
        }
    });
    },
    edit: function(req, res) {
    console.log(req.params.id);
    
    var cats = Cat.findByIdAndUpdate(req.params.id, {$set: req.body}, function(err, message){
        if (err) {
            console.log(err);
        } else {
            res.redirect('/');
        }
    });
    },
    destroy: function(req, res) {
    var cats = Cat.findByIdAndRemove(req.params.id, function(err,message){
        if (err) {
            console.log(err);
        } else {
            res.redirect('/');
        }
    });
    }
};
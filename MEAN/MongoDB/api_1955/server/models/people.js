var mongoose = require('mongoose');

var PeopleSchema = new mongoose.Schema({
    name: String,
});

mongoose.model('People', PeopleSchema);
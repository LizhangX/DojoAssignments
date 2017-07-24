let mongoose = require('mongoose');
let Note = mongoose.model('Note');

class NoteController{
    create(req,res){
        Note.create(req.body, (err, note) => {
            if (err) { return res.json(err); }
            return res.json(note);
        });
    }
    show(req,res){
        Note.find({}, (err, note) => {
            if (err) { return res.json(err); }
            return res.json(note);
        });
    }
}

module.exports = new NoteController();
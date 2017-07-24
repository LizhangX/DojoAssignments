let mongoose = require('mongoose');

let NoteSchema = new mongoose.Schema({
    note: {
        type: String,
        required: true,
        minlength: [3, 'at least 3 characters'],
    }
}, {timestamps: true});

mongoose.model('Note', NoteSchema);

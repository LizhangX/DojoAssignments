var mongoose = require('mongoose');

var CatSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, "Name cannot be blank"]
    },
    weight: {
        type: Number,
        required: [true, "Weight cannot be blank"]
    },
    color: {
        type: String,
        required: [true, "Color cannot be blank"]
    }
}, { timestamps: true });

mongoose.model('Cat', CatSchema);
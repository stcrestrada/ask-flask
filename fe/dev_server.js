var express = require('express');
var request = require('request');

var app = express();


app.use('/rest/', function (req, res){
    console.log(req);
    var url = "http://0.0.0.0:8000/api/v1/" + req.url;
    console.log(url);
    req.pipe(request(url)).pipe(res);
});

app.use(express.static(__dirname));
app.use(express.static('assets'));
app.use(express.static('app'));
app.listen(3000);

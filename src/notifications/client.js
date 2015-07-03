var io = require('socket.io-client');

var server = 'http://localhost:3000';
var socket = io(server);

socket.on('connect', function () {
  socket.on('message', function(msg) {
    console.log(msg);
  });
});

socket.on('error', function(msg) {
  console.error(msg);
});

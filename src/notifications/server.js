var http = require('http');

var server = http.createServer().listen(3000);
var io = require('socket.io')(server);

var cookie_reader = require('cookie');
var querystring = require('querystring');
var redis = require('redis');

// middleware to save the parsed cookies as data on the request
io.use(function(socket, next) {
    var data = socket.request;
    data.cookie = {};

    if(data.headers.cookie){
      data.cookie = cookie_reader.parse(data.headers.cookie);
    }

    next()
});

// connect the client to appropriate redis channels
var notifications = io
  .of('/notifications')
  .on('connection', function (socket) {
    console.log("Connecting client");
    client = redis.createClient(6379, 'localhost', {});

    // personal notification channels if logged in
    if(socket.request.cookie.session) {
      client.subscribe('notifications.' + socket.request.cookie.sessionid);
    }

    // broadcast channel subscription
    client.subscribe('notifications.broadcast');

    // forward publications on the redis channels to the socket client
    client.on('message', function(channel, message){
      socket.emit('message', message);
    });

    // unsubscribe after a disconnect event
    socket.on('disconnect', function () {
      console.log("Disconnected client");

      if(socket.request.cookie.session) {
        client.unsubscribe('notifications.' + socket.request.cookie.sessionid);
      }

      client.unsubscribe('notifications.broadcast');
    });
  });

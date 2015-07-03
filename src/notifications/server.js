var http = require('http');

var server = http.createServer().listen(3000);
var io = require('socket.io')(server);

var cookie_reader = require('cookie');
var querystring = require('querystring');
var redis = require('redis');

var redis_session_prefix = "csrdelft_session:";
var redis_port = 6379;
var redis_host = 'localhost';
var client = redis.createClient(redis_port, redis_host, {});

var { cookieMiddleware, sessionMiddleware, authMiddleware } = require('./middleware');

// cookie middleware
io.use(cookieMiddleware);
io.use(sessionMiddleware);
io.use(authMiddleware);

// connect the client to appropriate redis channels
var notifications = io
  .of('/notifications')
  .on('connection', function (socket) {
    var client = redis.createClient(redis_port, redis_host, {});
    console.log("Connected client: ", socket.request.session._auth_user_id);

    // personal notifications
    client.subscribe('notifications:' + socket.request.session._auth_user_id);
    // broadcast channel subscription
    client.subscribe('notifications:broadcast');

    // forward publications on the redis channels to the socket client
    client.on('message', function(channel, message){
      socket.emit('message', message);
    });

    // unsubscribe after a disconnect event
    socket.on('disconnect', function () {
      console.log("Disconnected client: ", socket.request.session._auth_user_id);

      if(socket.request.cookie.session) {
        client.unsubscribe('notifications.' + socket.request.cookie.sessionid);
      }

      client.unsubscribe('notifications.broadcast');
    });
  });

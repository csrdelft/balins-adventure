var http = require('http');

var server = http.createServer().listen(3000);
var io = require('socket.io')(server);

var cookie_reader = require('cookie');
var querystring = require('querystring');
var redis = require('redis');

var redis_session_prefix = "csrdelft_session:";
var redis_port = 6379;
var redis_host = 'localhost';

// cookie middleware
io.use(function(socket, next) {
    var data = socket.request;
    data.cookie = {};

    if(data.headers.cookie){
      data.cookie = cookie_reader.parse(data.headers.cookie);
    }

    next();
});

// session middleware
// makes 'session', 'isAuthenticated' available on the request object
io.use(function(socket, next) {
    var data = socket.request;
    data.isAuthenticated = false;
    data.session = {};

    var sessionid = data.cookie.sessionid;
    if(sessionid) {
      // get the session data
      var client = redis.createClient(redis_port, redis_host, {});
      client.get(redis_session_prefix + sessionid, function (err, djangoSessionData) {
        if (djangoSessionData) {
          var sessionData = new Buffer(djangoSessionData, 'base64').toString();
          var sessionObjString = sessionData.substring(sessionData.indexOf(":") + 1);
          var sessionObjJSON = JSON.parse(sessionObjString);

          // save it on the request
          data.session = sessionObjJSON;
          data.isAuthenticated = true;

          // proceed
          next();
        }
      });
    }
});

// don't allow users that aren't authenticated
io.use(function(socket, next) {
  if(!socket.request.isAuthenticated) {
    next(new Error("Forbidden"));
  } else {
    next();
  }
});

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

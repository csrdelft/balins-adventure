module.exports = {

  // parse the cookie and make it available on the request object
  cookieMiddleware: function(socket, next) {
    var data = socket.request;
    data.cookie = {};

    if(data.headers.cookie){
      data.cookie = cookie_reader.parse(data.headers.cookie);
    }

    // proceed
    next();
  },

  // session middleware
  // makes 'session', 'isAuthenticated' available on the request object
  sessionMiddleware: function(socket, next) {
    var data = socket.request;
    data.isAuthenticated = false;
    data.session = {};

    var sessionid = data.cookie.sessionid;
    if(sessionid) {
      // get the session data
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
  },

  // don't allow users that aren't authenticated
  authMiddleware: function(socket, next) {
    if(!socket.request.isAuthenticated) {
      // stop here with an error
      next(new Error("Forbidden"));
    } else {
      // proceed
      next();
    }
  }
};

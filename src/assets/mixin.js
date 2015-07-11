let assign = require('object-assign');

module.exports = function(base, ...mixins) {
  // create a new class
  class Class extends base {}

  assign(Class.prototype, ...mixins);

  return Class;
};

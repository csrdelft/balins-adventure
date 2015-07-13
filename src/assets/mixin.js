let assign = require('object-assign');

module.exports = function(base, ...mixins) {
  // create a new class
  class Class extends base {}

  // mixin the mixins into the prototype
  assign(Class.prototype, ...mixins);

  return Class;
};

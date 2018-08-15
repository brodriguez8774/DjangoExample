(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

/**
 * This file shows three separate ways of using React to render an H2 header with the words "Hello World!"
 */

/**
 * First way to render hello world.
 * As simple as possible, but must compile through browserify to work properly.
 */
var hello_world_header_1 = React.createElement(
  'h2',
  null,
  'Hello World! (Version 1)'
);

/**
 * Second way to render hello world.
 * Technically, this is what browserify compiles the above into.
 * It's not as friendly to read, but less hassle to get working (you don't need babel or browserify, etc).
 */
var hello_world_header_2 = React.createElement('h2', {}, 'Hello World! (Version 2)');

/**
 * Third way to render hello world.
 * I believe this is closer to the "standard" most people currently use.
 * Also requires browserify, but uses a class-based approach for front end elements.
 *
 * This method is advantageous for a few reasons. For example, the above two methods can only be exported with
 * "default". Each file can only have one default at a time. However, class based objects do not require default.
 * Thus a file can export multiple class based objects at once.
 */

var HelloWorldHeader3 = function (_React$Component) {
  _inherits(HelloWorldHeader3, _React$Component);

  function HelloWorldHeader3() {
    _classCallCheck(this, HelloWorldHeader3);

    return _possibleConstructorReturn(this, (HelloWorldHeader3.__proto__ || Object.getPrototypeOf(HelloWorldHeader3)).apply(this, arguments));
  }

  _createClass(HelloWorldHeader3, [{
    key: 'render',
    value: function render() {
      return React.createElement(
        'h2',
        null,
        'Hello World! (Version 3)'
      );
    }
  }]);

  return HelloWorldHeader3;
}(React.Component);

/**
 * Export statements.
 *
 * As stated above, each file can only export a single "default" object.
 * All non-class objects must be exported as "default".
 * Multiple class objects can be exported at once, using the syntax { obj_1, obj2, ... }.
 */


exports.default = hello_world_header_1;
//export default hello_world_header_2;

exports.HelloWorldHeader3 = HelloWorldHeader3;

},{}],2:[function(require,module,exports){
'use strict';

var _hello_world = require('./hello_world.js');

var _hello_world2 = _interopRequireDefault(_hello_world);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

/**
 * This is a basic react file.
 * It renders react components on the page, as long as it can find an element with id of "react-root".
 * Unfortunately, you will need to compile code using browserify. See readme for details.
 */

console.log('Loaded "react_example.js" file.');

// Import from hello world file.


var hello_world_header = _hello_world2.default;
//const hello_world_header = hello_world_header_2;
//const hello_world_header = <HelloWorldHeader3 />;


// Render to page.
ReactDOM.render(hello_world_header, document.getElementById('react-root'));

},{"./hello_world.js":1}]},{},[2]);

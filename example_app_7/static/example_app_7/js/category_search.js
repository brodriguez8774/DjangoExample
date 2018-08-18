(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

/**
 * This is loaded to supplement the "category_search.js" file.
 */

var Category = function (_React$Component) {
    _inherits(Category, _React$Component);

    /**
     * Constructor. Called on object creation.
     */
    function Category(props) {
        _classCallCheck(this, Category);

        return _possibleConstructorReturn(this, (Category.__proto__ || Object.getPrototypeOf(Category)).call(this, props));
    }

    /**
     * The elements rendered to the page.
     * Immediately renders category based on passed values.
     */


    _createClass(Category, [{
        key: "render",
        value: function render() {
            return React.createElement(
                "li",
                null,
                React.createElement(
                    "a",
                    { href: this.props.url },
                    "PK: ",
                    this.props.pk,
                    ", Title: ",
                    this.props.title,
                    ", DateCreated: ",
                    this.props.date_created,
                    ", DateModified: ",
                    this.props.date_modified
                )
            );
        }
    }]);

    return Category;
}(React.Component);

exports.default = Category;

},{}],2:[function(require,module,exports){
'use strict';

Object.defineProperty(exports, "__esModule", {
    value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _category = require('./category');

var _category2 = _interopRequireDefault(_category);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; } /**
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                * This is loaded to supplement the "category_search.js" file.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                */

var CategoryList = function (_React$Component) {
    _inherits(CategoryList, _React$Component);

    /**
     * Constructor. Called on object creation.
     */
    function CategoryList(props) {
        _classCallCheck(this, CategoryList);

        // Set default state.
        var _this = _possibleConstructorReturn(this, (CategoryList.__proto__ || Object.getPrototypeOf(CategoryList)).call(this, props));

        _this.state = {
            query: categories,
            initial_query: categories
        };
        return _this;
    }

    /**
     * Input box change handler. Loops through and filters all categories.
     */


    _createClass(CategoryList, [{
        key: 'handleChange',
        value: function handleChange(event) {
            var filtered_categories = [];
            this.state.initial_query.forEach(function (category, id) {
                if (category.fields['title'].toLowerCase().includes(event.target.value.toLowerCase())) {
                    filtered_categories.push(category);
                }
            });
            console.log({ filtered_categories: filtered_categories });
            this.setState({ query: filtered_categories });
        }

        /**
         * The elements rendered to the page.
         * First calculates what every individual category is. Then renders and returns full elements.
         */

    }, {
        key: 'render',
        value: function render() {
            var categories = [];
            this.state.query.forEach(function (category) {
                categories.push(React.createElement(_category2.default, {
                    key: category.pk,
                    pk: category.pk,
                    title: category.fields['title'],
                    url: category.fields['url'],
                    date_created: category.fields['date_created'],
                    date_modified: category.fields['date_modified']
                }));
            });

            return React.createElement(
                'div',
                null,
                React.createElement(
                    'label',
                    null,
                    'Search Categories: '
                ),
                React.createElement('input', {
                    type: 'text',
                    value: this.state.input,
                    placeholder: 'Search for...',
                    onChange: this.handleChange.bind(this)
                }),
                React.createElement(
                    'h2',
                    null,
                    'Categories'
                ),
                React.createElement(
                    'ul',
                    null,
                    categories
                )
            );
        }
    }]);

    return CategoryList;
}(React.Component);

exports.default = CategoryList;

},{"./category":1}],3:[function(require,module,exports){
'use strict';

var _category = require('./category');

var _category2 = _interopRequireDefault(_category);

var _category_list = require('./category_list');

var _category_list2 = _interopRequireDefault(_category_list);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

/**
 * This file is used as the core of the "category_search" page.
 */

console.log('Loaded category_search.js file.');
console.log(categories);

// React function to create list of categories.
function App() {
    return React.createElement(_category_list2.default, null);
}

// Render to page.
ReactDOM.render(App(), document.getElementById('react-root'));

},{"./category":1,"./category_list":2}]},{},[3]);

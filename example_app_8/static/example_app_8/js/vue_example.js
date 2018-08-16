/**
 * This is a basic vue file loaded on the index page.
 * It renders vue components on the page, as long as it can find an element with id of "vue-root".
 * Unfortunately, you will need to compile code using browserify. See readme for details.
 */


console.log('Loaded "vue_example.js" file.')


// Note: Django and Vue both want to use "{{ <value> }}" for rendering. To get past this limitation,
// we change Vue's rendering to use single brackets ("{ <value }") with the delimiters option.
var app = new Vue({
  delimiters: ['{', '}'],
  el: '#vue-root',
  data: {
    hello_world_header: 'Hello World!'
  }
})

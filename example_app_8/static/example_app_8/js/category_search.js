/**
 * This file is used as the core of the "category_search" page.
 */

console.log('Loaded "vue_example.js" file.')
console.log(categories)


Vue.component('category', {
    props: {
        category: Object
    },
    template: `
        <li>
            PK: {{ category.pk }} |&nbsp;
            Title: {{ category.fields.title }} |&nbsp;
            DateCreated: {{ category.fields.date_created }} |&nbsp;
            DateModified: {{ category.fields.date_modified }}
        </li>
    `,
})


var app = new Vue({
  delimiters: ['{', '}'],
  el: '#vue-root',
  data: {
    category_list: categories,
  }
})

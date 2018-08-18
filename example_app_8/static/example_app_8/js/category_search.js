/**
 * This file is used as the core of the "category_search" page.
 */

console.log('Loaded "vue_example.js" file.')
console.log(categories)


/**
 * A Vue object for a Category.
 */
Vue.component('category', {
    props: {
        category: Object
    },
    template: `
        <li>
            <a v-bind:href="category.fields.url">
                PK: {{ category.pk }} |&nbsp;
                Title: {{ category.fields.title }} |&nbsp;
                DateCreated: {{ category.fields.date_created }} |&nbsp;
                DateModified: {{ category.fields.date_modified }}
            </a>
        </li>
    `,
})


var app = new Vue({
    delimiters: ['{', '}'],
    el: '#vue-root',

    /**
     * The "variables" for Vue to hold. Anything not dynamically computed is defined here.
     */
    data: {
        search_value: '',
        initial_query: categories,
    },

    /**
     * The "computed" variables.
     * Do not define the same var both here and in data.
     */
    computed: {
            query() {
                return this.initial_query.filter(category => {
                    return category.fields['title'].toLowerCase().includes(this.search_value.toLowerCase())
            })
        }
    },
})

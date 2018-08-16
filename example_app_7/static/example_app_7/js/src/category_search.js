/**
 * This file is used as the core of the "category_search" page.
 */

import Category from './category';
import CategoryList from './category_list';

console.log('Loaded category_search.js file.');
console.log(categories);


// React function to create list of categories.
function App() {
    return (
      <div>
        <CategoryList categories={categories} />
      </div>
    );
}


// Render to page.
ReactDOM.render(
    App(),
    document.getElementById('react-root')
);

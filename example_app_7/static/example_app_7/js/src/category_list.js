/**
 * This is loaded to supplement the "category_search.js" file.
 */

import Category from './category';


class CategoryList extends React.Component {

    /**
     * Constructor. Called on object creation.
     */
    constructor(props) {
        super(props);

        // Set default state.
        this.state = {
            query: categories,
            initial_query: categories,
        }
    }

    /**
     * Input box change handler. Loops through and filters all categories.
     */
    handleChange(event) {
        const filtered_categories = [];
        this.state.initial_query.forEach((category, id) => {
            if (category.fields['title'].toLowerCase().includes(event.target.value.toLowerCase())) {
                filtered_categories.push(
                    category
                );
            }
        });
        console.log({ filtered_categories })
        this.setState({ query: filtered_categories });
    }

    /**
     * The elements rendered to the page.
     * First calculates what every individual category is. Then renders and returns full elements.
     */
    render() {
        const categories = [];
        this.state.query.forEach((category, id) => {
            categories.push(
                <Category
                    key={ category.pk }
                    pk={ category.pk }
                    title={ category.fields['title'] }
                    date_created={ category.fields['date_created'] }
                    date_modified={ category.fields['date_modified'] }
                />
            );
        });

        return (
            <div>
                <label>Search Categories: </label>
                <input
                    type="text"
                    value={ this.state.input }
                    placeholder="Search for..."
                    onChange={ this.handleChange.bind(this) }
                />
                <h2>Categories</h2>
                <ul>{ categories }</ul>
            </div>
        )
    }
 }

 export default CategoryList;

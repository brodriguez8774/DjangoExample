/**
 * This is loaded to supplement the "category_search.js" file.
 */

import Category from './category';

class CategoryList extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        const categories = [];
        this.props.categories.forEach((category, id) => {
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

        return <ul>{ categories }</ul>
    }
}

export default CategoryList;

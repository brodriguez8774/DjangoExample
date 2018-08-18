/**
 * This is loaded to supplement the "category_search.js" file.
 */

class Category extends React.Component {

    /**
     * Constructor. Called on object creation.
     */
    constructor(props) {
        super(props);
    }

    /**
     * The elements rendered to the page.
     * Immediately renders category based on passed values.
     */
    render() {
        return (
            <li>
                <a href = { this.props.url }>
                    PK: { this.props.pk },
                    Title: { this.props.title },
                    DateCreated: { this.props.date_created },
                    DateModified: { this.props.date_modified }
                </a>
            </li>
        )
    }
}

export default Category;

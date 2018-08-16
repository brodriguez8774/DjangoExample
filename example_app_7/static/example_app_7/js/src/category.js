/**
 * This is loaded to supplement the "category_search.js" file.
 */

class Category extends React.Component {
    constructor(props) {
        super(props);

//        this.pk = this.props.pk;
//        this.title = this.props.title;
//        this.date_created = this.props.date_created;
//        this.date_updated = this.props.date_updated;
    }

    render() {
        return <li>
            PK: { this.props.pk },
            Title: { this.props.title },
            DateCreated: { this.props.date_created },
            DateModified: { this.props.date_modified }
        </li>
    }
}

export default Category;

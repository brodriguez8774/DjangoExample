/**
 * This is a basic react file.
 * It renders react components on the page, as long as it can find an element with id of "react-root".
 */

console.log('Loaded "react-example.js" file.')

const hello_world_header = React.createElement(
    'h2',
    {},
    'Hello World!'
);


ReactDOM.render(
    hello_world_header,
    document.getElementById('react-root')
);

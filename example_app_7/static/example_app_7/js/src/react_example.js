/**
 * This is a basic react file loaded on the index page.
 * It renders react components on the page, as long as it can find an element with id of "react-root".
 * Unfortunately, you will need to compile code using browserify. See readme for details.
 */


console.log('Loaded "react_example.js" file.')


// Import from hello world file.
import hello_world_header_1 from './hello_world.js';
import hello_world_header_2 from './hello_world.js';
import {HelloWorldHeader3} from './hello_world.js';


const hello_world_header = hello_world_header_1;
//const hello_world_header = hello_world_header_2;
//const hello_world_header = <HelloWorldHeader3 />;


// Render to page.
ReactDOM.render(
    hello_world_header,
    document.getElementById('react-root')
);

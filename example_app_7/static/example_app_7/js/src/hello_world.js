/**
 * This file shows three separate ways of using React to render an H2 header with the words "Hello World!"
 */


/**
 * First way to render hello world.
 * As simple as possible, but must compile through browserify to work properly.
 */
const hello_world_header_1 = <h2>Hello World! (Version 1)</h2>;


/**
 * Second way to render hello world.
 * Technically, this is what browserify compiles the above into.
 * It's not as friendly to read, but less hassle to get working (you don't need babel or browserify, etc).
 */
const hello_world_header_2 = React.createElement(
    'h2',
    {},
    'Hello World! (Version 2)'
);


/**
 * Third way to render hello world.
 * I believe this is closer to the "standard" most people currently use.
 * Also requires browserify, but uses a class-based approach for front end elements.
 *
 * This method is advantageous for a few reasons. For example, the above two methods can only be exported with
 * "default". Each file can only have one default at a time. However, class based objects do not require default.
 * Thus a file can export multiple class based objects at once.
 */
class HelloWorldHeader3 extends React.Component {
    render() {
        return <h2>Hello World! (Version 3)</h2>;
    }
}


/**
 * Export statements.
 *
 * As stated above, each file can only export a single "default" object.
 * All non-class objects must be exported as "default".
 * Multiple class objects can be exported at once, using the syntax { obj_1, obj2, ... }.
 */
export default hello_world_header_1;
//export default hello_world_header_2;
export { HelloWorldHeader3 };

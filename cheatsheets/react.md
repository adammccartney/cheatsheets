some notes on react
===================

Many of the architectural principles are the same as with Vue. There are a
number of slight differences out of the box, mostly relating to usability of
the language/framework.

## JSX syntax
React seems to embrace the fact that rendering logic is inherently coupled to
other UI logic: how events are handled, how the state changes over time, and
how the data is prepared for display. React components are therefor essentially
javascript classes with lots of markup interwoven. This stands in contrast to
the Vue.js approach, where components are generally files with a .vue
extension, which contain up to three seperate segments: markup, script and
style.
Bear in mind that it might be useful to explicitly state with the filename
that a source file will contain jsx. This is the style guide recommendation at
AirBnB for instance.


## Emphasis on immutability

React emphasizes immutability as a way to facilitate the implementation of
complex features. For example, by using immutable objects, it is possible to
keep previous states of an app intact and to return to them easily.

## Function components

First class functions ?! woohoo!

The simplest way to define a react component is to declare a javascript
function and pass it a props (properties) object as argument.

```
function Welcome(props) {
    return <h1>Hello, {props.name}</h1>;
    }
```

## Converting functions to classes
Sometimes components will need to manage their own state, in these instances it
becomes necessary to use classes. There are five steps to convert a function to
a class:

1. Create an ES6 class, with the same name, that extends React.Component.
2. Add a single empty mehtod to it called render().
3. Move the body of the function into the render() method.
4. Replace props with this.props in the render() body.
5. Delete the remaining empty function declaration.


## State and Lifecycle

After introducing state by means of a class constructor, the next step towards
managing the lifecycle of the object is to declare two methods within the
class:
```
  componentDidMount() {
  }

  componentWillUnmount() {
  }
```
These are known as lifecylce methods. 

Components don't care if they are stateful or stateless

## Lists and keys

React has an unusual way of iterating over lists, it doesn't have an explicit
if and for loop, such as with v-for v-if. Instead it uses javascript's map 
function to unpack lists:
```
function NumberList(props) {
    const numbers = props.numbers;
    const listItems = numbers.map((number) => 
        <li key={number.toString()}>{number}</li>
    );
    return (
        <ul>{listItems}</ul>
    );
}
```

It's best practice in react to give individual array elements a key with which
they kan be identified. In most cases this will be the data.ID 

JSX allows for inline expressions:
```
function NumberList(props) {
  const numbers = props.numbers;
  return (
    <ul>
      {numbers.map((number) => 
        <ListItem key={number.toString()}
                  value={number} />
      )}
      </ul>
    );
}
```


## Handling events

React uses synthetic events, defined according to the [W3C spec][] it has a
[well defined API][] for dealing with all the various sorts of event.


[W3C spec]: https://www.w3.org/TR/DOM-Level-3-Events/
[well defined API]: https://reactjs.org/docs/events.html


## State management

If something can be derived from either props or state, then it probably
shouldn't be in state.

## The React state of mind
Useful doc on approaching UI design with react:
https://reactjs.org/docs/thinking-in-react.html

### Step 1: Break the UI into a component hierarchy
Identify all components present in the mocks, draw boxed around them and give
them all names. Furthermore, identify what data each component is representing.
Once they have all been identified, arrange them into a hierarchy.

### Step 2: Build a static version in React
It is generally advised creatie a UI render from the data model that does note
have any interactivity. This creates a conscious separation between UI look and
reactivity. The first reason for this separation lies in the fact that the
static model will require a lot of typing but not a lot of thinking, where as
the interactive model will require a lot of thinking and not a lot of typing.

### Step 3: Identify the minimal (but complete) representation of UI State
Apparently keeping it DRY is key.

Go through each component in your library and figure out which one is state.
Ask three questions about each piece of data:
1. Is it passed in from a parent via props? If so, it probably isn't state.
2. Does it remain unchanged over time? If so, it probably isn't state.
3. Can you compute it based on any other state or props in your component? If
   so, it isn't state.

### Step 4: Identify where your state should live
Keep in mind that react is all about one way data-flow down the component
hierarchy.

For each piece of state in the application:
+ identify every component that renders something based on that state.
+ Find a common owner component (a single component above all the components
  that need state in the hierarchy)
+ Either the common owner or another component higher up in the hierarchy
  shouild own the state.
+ If you can't find a component where it makes sense to own the state, create a
  new component solely for holding the state and add it somewhere in the
  hierarchy above the common owner component.


### Step 5: Add Inverse Data Flow
Components should only update their own state. This means that the highest
common component will be passing callbacks out to components elsewhere in the
hierarchy that fire whenever the state should be updated.


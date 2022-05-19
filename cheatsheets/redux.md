# redux


## overview

redux is a tool for global state management in react (I'm saying react, it's a
standalone library and can probably be used in a more modular way than I'm
giving it credit). It can possibly be interchanged with a library like
**vuex**. Anyway, the point being, all of these libraries are basically tools
or patterns for the management of global state in a js webapp. They all more or
less derive or build upon the original [flux](https://facebook.github.io/flux/)
design pattern.

## basics

Redux functions around the premise of "slices", logical units of organization
that contains the "reducer" logic and actions particular to a specific feature
of the Redux state. The API seems slightly more direct than vuex's comparable
"actions/getters/mutations", which seems to necessitate a bit more indirection
in order to make changes to global state -> and in vue2 appeared to be truely
"global". A slice in redux seemingly aims to be something like an "abstract
namespace" for global state. The way I understand this is that there are a
number of aspects that ideally are overridden in the definition of a `...Slice.js`
file. 


### naming conventions / organizational patterns

The structure demonstrated on the [redux website](https://redux.js.org/tutorials/essentials/part-2-app-structure)
favors creating a hierarchy as follows, which echoes patterns found in next.js
development (in terms of style in a local module) and also the well known
components trope.

```
src/features/
└── authenticator
    ├── Authenticator.js
    ├── Authenticator.module.css
    └── authenticatorSlice.js
```

## hooks

The more modern approach to redux leverages react hooks in order to avoid
situations where components might have to talk to the redux store directly.

+ `useSelector` to retrieve state from the store
+ `useDispatch` to dispatch a store's method (change state)


## rules of reducers

reducers are typically imported into the store after they have been defined in
their own `feature/${type}/${rname}Slice` module. Such a module will typically
define a number of actions. These actions are imported by their own names
elsewhere in the app, typically being called as a function with two args:
`(state, action)`

They are supposed to be pure: i.e. you're not supposed to be doing any API
calls etc. from inside a reducer. To do anything from within a reducer, that
code needs to live in a function called a `thunk`


## description of actions

1. plain object
2. has a type
3. whatever else you want
```
{
  type: "USER_LOGGED_IN",
  username: "adam"
}

```

Redux uses action creators: 

```
function userLoggedIn() {
    return {
      type: 'USER_LOGGED_IN',
      username: 'adam'
   };
}
```

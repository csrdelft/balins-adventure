# Client Architecture

This chapter focusses on the client.

## API communication

For the API communication we use a very simple library `q.xhr` based on the `q` implementation of
JS promises.

#### Promises??

Promises literally represent the promise that some data will become available in the future.
This is very useful for e.g. API communication, because we don't want to wait until the request
to the server is finished.
So we make the request asynchronously and return a promise that we will call you when the data is in.

Here are the [q.xhr docs](https://github.com/nathanboktae/q-xhr)
and here is our [api implementation](https://github.com/csrdelft/balins-adventure/blob/master/src/assets/scripts/utils/api.js).

## UIs using ReactJS

We build the interfaces using [ReactJS from facebook](https://facebook.github.io/react/).
A good start would be the tutorial.
We use the es6 syntax, which has a few differences with the syntax used in the tutorial.

The differences are described [here](https://facebook.github.io/react/blog/2015/01/27/react-v0.13.0-beta-1.html)
and we have written the tutorial in that syntax in [the react-tutorial branch](https://github.com/csrdelft/balins-adventure/blob/react-tutorial/src/assets/app.jsx).

We use ReactJS for a few reasons:

1. It does UI *only*. The Unix rule of software is: do one thing only and do that thing really well.
2. It has unidirectional data flow. You are only concerned with two things: state updates and how
   to render html from a state. React worries about efficiency of DOM updates and what not.
3. It is becoming the standard for fast UIs on the client; lots of fun stuff we can reuse.
4. Good tooling (e.g. the chrome debug plugin)

#### Client Side Routing

To determine which client side page we want to render, we use [react-router](http://rackt.github.io/react-router/#RouteHandler).
It has the same function as the server side router: it looks at the route and then renders the
specified handler, passing it any url parameters as react properties.

All you have to know about routes is in [here](https://github.com/csrdelft/balins-adventure/blob/master/src/assets/scripts/routes/index.js).
Links are created with the `<Link to="some/path/to/somwhere" />` component from the `react-router` module.

#### Props? State? Updating?

Sooo, components have both properties and state.
Properties are passed to them from their parent (like regular html attributes really).
State can be initialized from the properties but it's something that the component manages itself.
Properties should **never** be updated from within the component (React will warn you if you do).

`render()` will be called by react on both property and state changes.
If you have to update the state when a property changes, you can do this using the
`componentWillReceiveProps(Object nextProps)` handler on the component.

More reading can be found [here](https://github.com/uberVU/react-guide/blob/master/props-vs-state.md).

#### Flux & Redux

To manage the state on the client we use the Flux architecture from Facebook.
The goal of this architecture is to prevent spaghetti code due to state pileup in different places.
If you worked with heavy clients in the browser before you know this is a risk: many components manage parts of the state, and will eventually all rely on each other. Terrible.

So Flux (and the implementation Redux in particular) manage this inversely: a global, central *store* manages all the application state.
The state is updated in response to actions, which act as global *events*. 
Actions are fired using `dispatch(event(eventParameters))` and may fire other events in effect. 

Actions are just objects that carry some data and may be caught by so called *reducers*, who are in charge of modifying the store in response to actions.
They are just functions that take the current store state and an action and return a new state.

Finally it's worthwile to point out that UI components fall in one of two categories: smart components (aka containers) and dumb ones (from now on just referred to as components):

- (Dumb) Components do not ask for state from the store and are unaware of Redux/Flux/The store in general.
- Containers *are* connected to the store using the function `connect`. Connect will inject part of the store state into the component as props. When the store changes (because action > reducer > change) the component will automagically update itself.

## Push notifications

TODO

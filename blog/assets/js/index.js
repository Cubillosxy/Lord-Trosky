import App from './component/app';
import React from 'react' ;
import ReactDOM from 'react-dom';
import store from './store';
import {Provider} from 'react-redux';

const root = document.getElementById('react-app');

const render = Component => {
  ReactDOM.render(
      <Provider store={store}>
          <Component/>
      </Provider>
      , root);
};

render(App);

if (module.hot) {
    module.hot.accept('./component/app.js', () => {
      const mainContainer = require('./component/app').default;
      render(mainContainer)
    })
}

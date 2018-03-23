/**
 * Created by Edwin C on 21/12/17.
 */

let webpack = require('webpack');


let config = require('./webpack.base.config.js');

config.entry = [
  'babel-polyfill',
  'react-hot-loader/patch',
   'webpack/hot/only-dev-server',
  './assets/js/index',
];

config.output.filename = 'app.bundle.js';
config.devServer.hot = true;

config.plugins = config.plugins.concat([
  new webpack.HotModuleReplacementPlugin(),
]);

module.exports = config;

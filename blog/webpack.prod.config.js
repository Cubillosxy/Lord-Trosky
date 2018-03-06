/**
 * Created by Edwin C on 21/12/17.
 */
let webpack = require('webpack');
let BundleTracker = require('webpack-bundle-tracker');

let config = require('./webpack.base.config.js');

config.output.path = require('path').resolve('./static/dist');

config.plugins = config.plugins.concat([
  new BundleTracker({filename: './webpack-stats-dashboard-prod.json'}),

  // removes a lot of debugging code in React
  new webpack.DefinePlugin({
    'process.env': {
      'NODE_ENV': JSON.stringify('production')
  }}),

  // keeps hashes consistent between compilations

  // minifies your code
  new webpack.optimize.UglifyJsPlugin({
    compressor: {
      warnings: false
    }
  })
]);

// Add a loader for JSX files
config.module.loaders.push(
  { test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel' }
);

module.exports = config;

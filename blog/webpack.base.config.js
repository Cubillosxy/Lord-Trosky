/**
 * Created by Edwin C on 21/12/17.
 */
let path = require("path");

module.exports = {
  context: __dirname,

  entry: './assets/js/index',

  output: {
      path: path.resolve('./assets/bundles/'),
      filename: "[name]-[hash].js"
  },
 devServer: {
    hot: false,
    },

  plugins: [
  ], // add all common plugins here


  module: {
     loaders: [{
      test: /\.js$/,
      loaders: ['react-hot', 'babel'],
      include: path.join(__dirname, 'src')
    }],
    rules: [
        {
          // test: que tipo de archivo quiero reconocer,
          // use: que loader se va a encargar del archivo
          test: /\.(js|jsx)$/,
          exclude: /(node_modules)/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['es2015', 'react', 'stage-2'],
            }
          },
        },
        {
          test: /\.css$/,
          use : ['style-loader', 'css-loader']
        },
        {
          test: /\.(jpg|png|gif|svg)$/,
          use: {
            loader: 'url-loader',
            options: {
              limit: 10000,
              fallback: 'file-loader',
              name: 'images/[name].[hash].[ext]',
            }
          }
        },
    ]
  },
};

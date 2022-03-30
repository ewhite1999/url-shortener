const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const ROOT_DIRECTORY = path.join(__dirname, '../');
const PUBLIC_DIRECTORY = path.join(ROOT_DIRECTORY, 'public');

const config = {
  entry: [path.resolve(ROOT_DIRECTORY, 'src/index.js')],
  output: {
    path: path.resolve(ROOT_DIRECTORY, 'dist'),
    filename: 'bundle.js',
    publicPath: '/',
  },
  mode: 'development',
  resolve: {
    modules: [path.resolve('node_modules'), 'node_modules']
  },
  performance: {
    hints: false,
  },
  plugins: [
    new HtmlWebpackPlugin ({
      template: path.join(PUBLIC_DIRECTORY, 'index.html'),
    }),
  ],
  module: {
    rules: [
      { 
        test: /\.(js|jsx)$/,
        resolve: {
          extensions: ['.js', '.jsx']
        },
        exclude: /node_modules/,
        loader: 'babel-loader'
      },
      { 
        test: /\.(css)$/,
        use: ['style-loader', 'css-loader'],
      }, 
      { 
        test: /\.(png|jpg|jpeg|pdf|ico)$/,
        resolve: {
          extensions: ['.ico', '.jpeg']
        },
        loader: ['file-loader'],
      }, 
    ]
  }
}

module.exports = config;

const config = require('./webpack.config')

config.devServer = {
  historyApiFallback: true,
  port: 8080,
  liveReload: true,
  open: true,
}

config.devtool = 'inline-source-map';

module.exports = config;

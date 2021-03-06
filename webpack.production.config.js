var path = require('path');
var webpack = require('webpack');
var autoprefixer = require('autoprefixer');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  entry: [
    './src/index'
  ],
  output: {
    path: path.join(__dirname, 'static'),
    filename: 'bundle.js',
    publicPath: '/static/'
  },
  plugins: [
      new ExtractTextPlugin('spec.css', {allChunks: true}),
	  new webpack.ProvidePlugin({
		  'fetch': 'imports?this=>global!exports?global.fetch!whatwg-fetch'
	  }),
	  new webpack.optimize.UglifyJsPlugin(),
	  new webpack.optimize.DedupePlugin()
  ],
  resolve: {
      extensions: ['', '.jsx', '.scss', '.js', '.json']
  },
  module: {
      loaders: [
	  {
	      test: /\.js$/,
	      loaders: ['babel'],
	      include: path.join(__dirname, 'src')
	  },
	  {
	      test:/\.css$/,
	      loader: ExtractTextPlugin.extract('style-loader', 'css-loader')
	  },
	  {
	      test: /\.scss$/,
	      // loader: ExtractTextPlugin.extract('style', 'css?sourceMap&modules&importLoaders=1&localIdentName=[name]__[local]___[hash:base64:5]!postcss!sass?sourceMap')

	      loader: ExtractTextPlugin.extract('style-loader', 'css-loader!sass-loader')

	      // loader: 'style-loader!css-loader!postcss-loader',
	  },
      ]
  },
  postcss: [autoprefixer],
};

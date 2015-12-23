var path = require('path');
var webpack = require('webpack');
var autoprefixer = require('autoprefixer');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  entry: [
    './src/index'
  ],
  devtool: 'eval-source-map', 
  output: {
    path: path.join(__dirname, 'build'),
    filename: 'bundle.js',
    publicPath: '/build/'
  },
  plugins: [
      new ExtractTextPlugin('spec.css', {allChunks: true}),
	  new webpack.ProvidePlugin({
		  'fetch': 'imports?this=>global!exports?global.fetch!whatwg-fetch'
	  })
  ],
  resolve: {
      extensions: ['', '.jsx', '.scss', '.js', '.json']
  },
  module: {
      loaders: [
	  {
	      test: /\.js$/,
	      loaders: ['react-hot', 'babel'],
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
	  }
      ]
  },
  postcss: [autoprefixer],
};

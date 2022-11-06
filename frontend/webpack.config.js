const HtmlWebpackPlugin = require('html-webpack-plugin');
const HtmlWebpackSkipAssetsPlugin = require('html-webpack-skip-assets-plugin').HtmlWebpackSkipAssetsPlugin;
const path = require('path');

module.exports = {
  mode: 'development',
  entry: './src/index.js', // update the entry path if necessary
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
    publicPath: '/',
  },
  devServer: {
    hot: true,
    open: true,
    historyApiFallback: true,
    port: 3000, // You can choose the port you want
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react'],
            plugins: [
              '@babel/plugin-transform-runtime',
              ['import', { libraryName: 'antd', style: 'css' }],
            ],
          },
        },
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.less$/,
        use: [
          'style-loader', // creates style nodes from JS strings
          'css-loader',   // translates CSS into CommonJS
          {
            loader: 'less-loader',
            options: {
              lessOptions: {
                javascriptEnabled: true,
              },
            },
          },
        ],
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html',
      filename: 'index.html', // the output file name that will be created in the dist folder
    }),
    // // Only use the SkipAssetsPlugin if you actually want to skip some assets
    // new HtmlWebpackSkipAssetsPlugin({
    //   // specify assets to skip here if necessary
    // }),
  ],
  // plugins: [
  //   new HtmlWebpackSkipAssetsPlugin({
  //     template: './public/index.html', // update the path to your index.html if necessary
  //   }),
  // ],
  resolve: {
    extensions: ['.js', '.jsx'], // resolve these extensions
  },
};

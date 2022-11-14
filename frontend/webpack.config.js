const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

module.exports = (env, argv) => {
  const isProduction = argv.mode === 'production';

  console.log(`Building frontend for environment ${process.env.HUPRES_ENV} at ${process.env.HUPRES_PROD_HOSTNAME}:${process.env.HUPRES_APP_PORT}`);

  return {
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
                ['import', {libraryName: 'antd', style: 'css'}],
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
        favicon: './public/favicon.ico',
      }),
      // new webpack.DefinePlugin(envKeys),
      new webpack.DefinePlugin({
        'process.env.HUPRES_ENV': JSON.stringify(process.env.HUPRES_ENV ?? isProduction ? 'production' : 'development'),
        'process.env.HUPRES_APP_PORT': JSON.stringify(process.env.HUPRES_APP_PORT),
        'process.env.HUPRES_PROD_HOSTNAME': JSON.stringify(process.env.HUPRES_PROD_HOSTNAME),
      })
    ],
    resolve: {
      extensions: ['.js', '.jsx'], // resolve these extensions
    },
  }
}

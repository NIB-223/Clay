// Misc
const path = require('path');

// Plugins
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const ManifestPlugin = require('webpack-manifest-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = env => {
    // Settings
    const dev = env.NODE_ENV === 'dev';
    const mode = dev ? 'development' : 'production';
    const entries = {
        app: ['./static/src/js/app.js', './static/src/css/app.scss']
    };
    const output = '/static/dist/';

    let postcss_options = {
        ident: 'postcss',
        plugins: [
            require('autoprefixer')({
                browsers: ['> 0%']
            })
        ]
    };

    if (!dev) {
        postcss_options.plugins.push(
            require('cssnano')({
                preset: 'default'
            })
        )
    }

    let cssLoaders = [
        {
            loader: MiniCssExtractPlugin.loader
        },
        {
            loader: 'css-loader',
            options: {
                importLoaders: 1,
                sourceMap: dev
            }
        },
        {
            loader: 'postcss-loader',
            options: postcss_options
        }
    ];

    // Actual config
    let config = {
        entry: entries,
        watch: dev,
        mode: mode,
        output: {
            path: path.resolve("." + output),
            filename: dev ? '[name].js' : '[name].[chunkhash:8].js',
            publicPath: output
        },
        devtool: dev ? 'cheap-module-eval-source-map' : false,
        module: {
            rules: [
                {
                    test: /\.js$/,
                    exclude: /(node_modules|bower_components)/,
                    use: [
                        {loader: 'babel-loader'}
                    ]
                },
                {
                    test: /\.css$/,
                    use: cssLoaders
                },
                {
                    test: /\.scss$/,
                    use: [
                        ...cssLoaders,
                        {loader: 'sass-loader', options: {sourceMap: dev}}
                    ]
                },
                {
                    test: /\.(png|jpe?g|gif|svg|ttf|otf|eot|woff2?)(\?.*)?$/,
                    use: [
                        {
                            loader: 'url-loader',
                            options: {
                                limit: 8192,
                                name: dev ? '[name].[ext]':'[name].[hash:8].[ext]',
								outputPath: 'assets/',
								publicPath: 'assets/'
                            }
                        }
                    ]
                }
            ]
        },
        plugins: [
            new MiniCssExtractPlugin({
                filename: dev ? '[name].css' : '[name].[hash:8].css',
                chunkFilename: dev ? '[id].css' : '[id].[hash:8].css',
            }),
            new ManifestPlugin({
                generate: (seed, files, entrypoints) => files.reduce((manifest, {name, path}) => ({...manifest, [name]: path.substring(1)}), seed)
            }),
        ]
    };
    if (!dev) {
        config.plugins.push(new CleanWebpackPlugin({
            root: path.resolve('./'),
            verbose: !dev,
            dry: false
        }))
    }
    return config;
};

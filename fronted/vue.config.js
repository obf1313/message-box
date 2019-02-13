const webpack = require('webpack')
const ExtractTextPlugin = require("extract-text-webpack-plugin")
module.exports = {
    publicPath: process.env.NODE_ENV === 'production' //部署应用包时的基本URL
        ? '/production/'
        : '/',
    outputDir: 'build', //生产环境构建文件的目录
    productionSourceMap: true,
    configureWebpack: {
        plugins: [
            new ExtractTextPlugin({
                filename:  "meehoo.css",
                allChunks: true
            }),
            new webpack.DefinePlugin({
                'process.env.NODE_ENV': JSON.stringify('production')
            })
        ],
        optimization: {
            splitChunks: {
                cacheGroups: {
                    vendor:{//node_modules内的依赖库
                        chunks:"all",
                        test: /[\\/]node_modules[\\/]/,
                        name:"vendor",
                        minChunks: 1, //被不同entry引用次数(import),1次的话没必要提取
                        maxInitialRequests: 5,
                        minSize: 0,
                        priority:100,
                        // enforce: true?
                    }
                }
            }
        }
    },
    devServer: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:8000',
                changeOrigin: true,// needed for virtual hosted sites
                ws: true,// proxy websockets
                pathRewrite: {
                    '^/api': ''
                }
            }
        }
    }
}

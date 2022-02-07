const CopyPlugin = require("copy-webpack-plugin");

const NodeEnv = process.env.NODE_ENV;
if (NodeEnv === "development") {
    publicPath = ""
} else {
    publicPath = "";
}
module.exports = {
    configureWebpack: {
        plugins: [
            new CopyPlugin([
                {from: "../reader/gen", to: "gen"},
            ]),
        ]
    },
    publicPath: publicPath,
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:8000',
                ws: true,
                changeOrigin: true
            },
        }
    }
}
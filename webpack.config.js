const path = require('path');

module.exports = {
    mode: 'development',
    entry: './src/index.js',　//buildするファイル
    output: {
        filename: 'bundle.js',　//build後のファイル名
        path: path.join(__dirname, '../step-to-goal/myapp/static/js'), //buildファイルが作成される場所
        publicPath: '/js/',
      },
    module: {
        rules: [
          {
            test: /\.css$/,  // CSSファイルを処理するための正規表現
            use: ['style-loader', 'css-loader'],  // 使用するローダーの指定
          },
          {
            test: /\.js[x]?$/,  
            exclude: /node_modules/,
            use: [
              {
                loader: 'babel-loader',
                options: {
                  presets: [
                    '@babel/preset-env',
                    ['@babel/preset-react', {"runtime": "automatic"}]
                  ],
                  plugins: ['@babel/plugin-syntax-jsx'] 
                }
              },
            ]
          }
        ]
      },
      resolve: {
        extensions: ['.js', '.jsx', '.json']
      }
};

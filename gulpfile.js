var gulp = require('gulp'),
    gutil = require('gulp-util'),
    sass = require('gulp-sass'),
    rename = require('gulp-rename'),
    path = require('path'),
    watch = require('gulp-watch'),
    source = require('vinyl-source-stream'),
    livereload = require('gulp-livereload'),
    notify = require('gulp-notify'),
    watchify = require('watchify'),
    browserify = require('browserify'),
    babelify = require('babelify');

var assets = path.join(__dirname, 'src/assets');
var fonts = path.join(assets, 'fonts/**/*');
var images = path.join(assets, 'images/**/*');
var dist = path.join(__dirname, 'dist');

gulp.task('sass', function() {
  gulp.src('./src/assets/sass/app.sass')
    .pipe(sass({
      includePaths : [
        path.join(__dirname, 'src/assets/fonts'),// sass
        path.join(__dirname, 'src/assets/sass'), // sass
        path.join(__dirname, 'src/assets/css'),  // css
        path.join(__dirname, 'node_modules/')    // libs
      ]
    }).on('error', sass.logError))
    .pipe(gulp.dest(path.join(dist, 'css')));
});

// initiates the scripts bundler
function compileScripts(watch) {
  var entryFile = path.join(assets, 'scripts/index.jsx');

  // we use browserify to bundle node style modules into a
  // script ready for the browser
  var bundler = browserify({
    entries: [entryFile],
    debug: true,
    paths: ['./node_modules/', path.join(assets, 'scripts'), assets],
    extensions: ['.jsx', '.js'],
    cache: {}, packageCache: {}, fullPaths: true,
    sourceMaps: true
  });

  // we use babel to transpile es6 syntax and the react jsx syntax
  // down to es5
  bundler.transform(babelify, {presets: ['es2015', 'react']});

  function bundle() {
    var stream = bundler
      .bundle()
      .on("error", notify.onError({
          message: "Error: <%= error.message %>",
          title: "Error building scripts"
      }))
      .pipe(source(entryFile))
      .pipe(rename('index.js'))
      .pipe(gulp.dest(path.join(dist, 'scripts')));

    stream.on('end', function() { gutil.log("Done building scripts"); });

    return stream;
  };

  // use watchify for fast rebuilds using browserify
  if(watch) {
    bundler = watchify(bundler);
    bundler.on('update', bundle);
  }

  return bundle();
}

// watch assets and build on changes
gulp.task('watch', function() {
  livereload.listen();

  function initWatch(files, task) {
    gulp.start(task);
    gulp.watch(files, [task]);
  }

  compileScripts(true);
  initWatch(['./src/assets/sass/**/*.sass', './src/assets/sass/**/*.css'], 'sass');
});

// copy the assets to the dist
gulp.task('copy', function() {
  return gulp.src([fonts, images], {base: assets})
    .pipe(gulp.dest(dist));
});

// run the tasks and start watching by default
gulp.task('default', function() {
  gutil.log(">> Building & standing watch for changes...");
  gulp.start('sass');
  gulp.start('copy');
  compileScripts(false);
  gulp.start('watch');
});

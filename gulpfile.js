var gulp = require('gulp'),
    gutil = require('gulp-util'),
    sass = require('gulp-sass'),
    rename = require('gulp-rename'),
    path = require('path'),
    watch = require('gulp-watch'),
    watchify = require('watchify'),
    browserify = require('browserify'),
    es6ify = require('es6ify'),
    reactify = require('reactify'),
    source = require('vinyl-source-stream'),
    livereload = require('gulp-livereload');

var assets = path.join(__dirname, 'src/assets');
var fonts = path.join(assets, 'fonts/**/*');
var images = path.join(assets, 'images/**/*');
var dist = path.join(assets, 'dist');

gulp.task('sass', function() {
  gulp.src('./src/assets/sass/app.sass')
    .pipe(sass({
      includePaths : [
        path.join(__dirname, 'src/assets/sass'), // sass
        path.join(__dirname, 'src/assets/css')   // css
      ]
    }))
    .pipe(gulp.dest(path.join(dist, 'css')));
});

function compileScripts(watch) {
  gutil.log('Starting browserify');

  var entryFile = './src/assets/app.jsx';
  es6ify.traceurOverrides = {experimental: true};

  var bundler = browserify(entryFile);
  bundler.require('./node_modules/react/react.js');
  bundler.transform(reactify);
  bundler.transform(es6ify.configure(/.jsx/));

  var rebundle = function () {
    var stream = bundler.bundle();

    stream.on('error', function (err) { console.error(err) });
    stream = stream.pipe(source(entryFile));
    stream.pipe(rename('app.js'));

    stream.pipe(gulp.dest(path.join(dist, 'scripts')));
  }

  if(watch) {
    bundler = watchify(bundler);
    bundler.on('update', rebundle);
  }

  return rebundle();
}

gulp.task('watch', function() {
  livereload.listen();

  function initWatch(files, task) {
    gulp.start(task);
    gulp.watch(files, [task]);
  }

  compileScripts(true);
  initWatch('./src/assets/sass/**/*.sass', 'sass');

  gulp.watch([dist + '/**/*']);
});

gulp.task('copy', function() {
  return gulp.src([fonts, images], {base: assets})
    .pipe(gulp.dest(dist));
});

gulp.task('default', function() {
  gulp.start('sass');
  gulp.start('copy');
  compileScripts(false);
  gulp.start('watch');
});

var gulp = require('gulp'),
    sass = require('gulp-sass'),
    path = require('path')
    watch = require('gulp-watch');

gulp.task('sass', function() {
  gulp.src('./src/assets/sass/app.sass')
    .pipe(sass({
      includePaths : [
        path.join(__dirname, 'src/assets/sass'), // sass
        path.join(__dirname, 'src/assets/css')   // css
      ]
    }))
    .pipe(gulp.dest('src/assets/css'));
});

gulp.task('watch', function() {
  watch('./src/assets/sass/**/*.sass', function() {
    gulp.start('sass');
  });
});

gulp.task('default', function() {
  gulp.run('sass');
  gulp.run('watch');
});

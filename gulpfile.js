var gulp = require('gulp'),
    compass = require('gulp-compass'),
    path = require('path')
    watch = require('gulp-watch');

gulp.task('compass', function() {
  gulp.src('./src/assets/sass/app.sass')
    .pipe(compass({
      project: path.join(__dirname, 'src/assets'),
      css: 'css',
      sass: 'sass'
    }))
    .pipe(gulp.dest('src/assets/css'));
});

gulp.task('watch', function() {
  watch('./src/assets/sass/**/*.sass', function() {
    gulp.start('compass');
  });
});

gulp.task('default', function() {
  gulp.run('watch');
});

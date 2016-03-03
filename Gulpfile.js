var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('styles', function() {
    gulp.src('letsjustbehonest/sass/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('static/css/'));
});

gulp.task('default',function() {
    gulp.watch('letsjustbehonest/sass/**/*.scss',['styles']);
});

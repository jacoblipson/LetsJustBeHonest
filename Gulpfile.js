var gulp = require('gulp');
var sass = require('gulp-sass');
var babel = require('gulp-babel');


gulp.task('sass', function() {
    gulp.src('letsjustbehonest/sass/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('static/css/'));
});

gulp.task('babel', function() {
    gulp.src('letsjustbehonest/static/react-src/**/*.js')
        .pipe(babel({
			presets: ['react']
		}))
        .pipe(gulp.dest('static/react-build/'));
});

gulp.task('default',function() {
    gulp.watch('letsjustbehonest/sass/**/*.scss',['sass']);
    gulp.watch('letsjustbehonest/static/react-src/**/*.js',['babel']);
});

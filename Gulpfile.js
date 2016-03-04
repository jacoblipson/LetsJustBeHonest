var gulp = require('gulp');
var sass = require('gulp-sass');
var babel = require('gulp-babel');

var project_root = 'letsjustbehonest/'

gulp.task('sass', function() {
    gulp.src(project_root+'sass/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest(project_root+'static/css/'));
});

gulp.task('babel', function() {
    gulp.src(project_root+'static/react-src/**/*.js')
        .pipe(babel({
			presets: ['react']
		}))
        .pipe(gulp.dest(project_root+'static/react-build/'));
});

gulp.task('default',function() {
    gulp.watch(project_root+'sass/**/*.scss',['sass']);
    gulp.watch(project_root+'static/react-src/**/*.js',['babel']);
});

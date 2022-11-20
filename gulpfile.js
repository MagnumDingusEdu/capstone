const autoprefixer = require('gulp-autoprefixer');
const del = require('del');
const cssbeautify = require('gulp-cssbeautify');
const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const wait = require('gulp-wait');
const sourcemaps = require('gulp-sourcemaps');

const paths = {
    css: './website/static/dist/css',
    scss: './scss'
};


// Beautify CSS
gulp.task('beautify:css', function () {
    return gulp.src([
        paths.css + '/scholarship-portal.css'
    ])
        .pipe(cssbeautify())
        .pipe(gulp.dest(paths.css))
});

// Minify CSS
gulp.task('minify:css', function () {
    return gulp.src([
        paths.css + '/scholarship-portal.min.css'
    ])
        .pipe(gulp.dest(paths.css))
});


// Clean
gulp.task('clean', function () {
    return del([paths.css], {force: true});
});


// Compile and copy scss/css
gulp.task('copy:dist:css', function () {
    return gulp.src([paths.scss + '/volt/**/*.scss', paths.scss + '/custom/**/*.scss', paths.scss + '/scholarship-portal.scss'])
        .pipe(wait(500))
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer({
            overrideBrowserslist: ['> 1%']
        }))
        .pipe(sourcemaps.write('.', {includeContent: false, sourceRoot: paths.scss}))
        .pipe(gulp.dest(paths.css))
});


gulp.task('build:dist', gulp.series('clean', 'copy:dist:css', 'beautify:css'));

gulp.task('serve', gulp.series('build:dist', function () {

    gulp.watch([paths.scss + '/volt/**/*.scss', paths.scss + '/custom/**/*.scss', paths.scss + '/volt.scss'], gulp.series('build:dist'));

}));
// Default
gulp.task('default', gulp.series('serve'));

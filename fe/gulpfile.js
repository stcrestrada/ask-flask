var gulp = require('gulp');
var nodemon = require('gulp-nodemon');
var jshint = require('gulp-jshint');
var stylish = require('jshint-stylish');
var connect = require('gulp-connect');

gulp.task('develop', function () {
    nodemon(
        {
            script: 'dev_server.js',
            ext: 'html, js',
            ignore: ['assets/*']
        })
        .on('restart', function () {
            console.log('server restarted');
        });
});
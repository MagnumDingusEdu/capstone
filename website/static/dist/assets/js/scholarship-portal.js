"use strict";
const d = document;
d.addEventListener("DOMContentLoaded", function (event) {


    // options
    const breakpoints = {
        sm: 540,
        md: 720,
        lg: 960,
        xl: 1140
    };

    const sidebar = document.getElementById('sidebarMenu');
    if (sidebar && d.body.clientWidth < breakpoints.lg) {
        sidebar.addEventListener('shown.bs.collapse', function () {
            document.querySelector('body').style.position = 'fixed';
        });
        sidebar.addEventListener('hidden.bs.collapse', function () {
            document.querySelector('body').style.position = 'relative';
        });
    }


    const scroll = new SmoothScroll('a[href*="#"]', {
        speed: 500,
        speedAsDuration: true
    });

    if (d.querySelector('.current-year')) {
        d.querySelector('.current-year').textContent = new Date().getFullYear().toString();
    }


});
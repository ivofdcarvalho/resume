let slideIndex = 0;
let paused = false;
let slides = document.getElementsByClassName("slide-card");
let dots = document.getElementsByClassName("slide-dot");

function protectIndex() {
    if (slideIndex > slides.length) {
        slideIndex = 1
    }
    if (slideIndex < 1) {
        slideIndex = slides.length
    }
}

// Next/previous controls
function control(n) {
    slideIndex += n;
    protectIndex()
    showSlides();
    paused = true;
}

function navigate(n) {
    slideIndex = n;

    protectIndex()
    showSlides();
    paused = true;
}

function autoSlide() {
    if (!paused) {
        slideIndex++;

        protectIndex()
        showSlides()
        setTimeout(autoSlide, 5000); // Change image every 5 seconds
    }
}

function showSlides() {
    // Hide everything and change style for all the dots
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
        dots[i].className = dots[i].className.replace(" active", "");
    }
    // Show selected and change style for the corresponding dot
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}
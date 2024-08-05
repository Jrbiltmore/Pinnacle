
document.addEventListener("DOMContentLoaded", function() {
    console.log("Tap'n'Earn Web App Loaded");

    const signupButton = document.querySelector("button");
    if (signupButton) {
        signupButton.addEventListener("click", navigateToSignup);
    }
});

function navigateToSignup() {
    window.location.href = "/signup.html";
}

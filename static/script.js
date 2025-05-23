document.addEventListener("DOMContentLoaded", function () {
    const video = document.getElementById("background-video");

    // handle safari specific behavior
    video.addEventListener('loadeddata', function() {
        // safari often needs a user gesture to play, but we'll try anyway
        if (video.paused) {
            try {
                // since its local we wait for a moment before playing the video
                setTimeout(() => {
                    video.play().catch(e => {
                        // on safari, this might fail due to autoplay restrictions
                        console.log("autoplay prevented by browser", e);
                    });
                    video.style.filter = "blur(0px)";
                }, Math.floor(Math.random() * (500 - 200 + 1)) + 200);
            } catch (e) {
                console.log("error playing video", e);
            }
        } else {
            // if already playing, just remove the blur
            video.style.filter = "blur(0px)";
        }
    });

    // add a backup for user interaction to play video (in case autoplay fails)
    document.addEventListener('click', function() {
        console.log('user clicked');
        if (video.paused) {
            video.play().catch(e => console.log("error playing video on click", e));
            video.style.filter = "blur(0px)";
        }
    }, { once: true });
});
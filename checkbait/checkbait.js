VIDEO_WATCH = "https://www.youtube.com/watch?";
VIDEO_SEARCH = "https://www.youtube.com/results?";
VIDEO_HOME = "https://www.youtube.com";
VIDEO_TRENDING = "https://www.youtube.com/feed/trending";
windowURL = window.location.href;
alert("fuck you");
getBaitLinks();
if(windowURL.includes(VIDEO_WATCH)) {
    videos = document.querySelectorAll("a.yt-simple-endpoint.style-scope.ytd-compact-video-renderer");
    turnRed(videos, getBaitLinks(getLinks(video)), VIDEO_WATCH);
}
else {
    if(windowURL.includes(VIDEO_SEARCH) || windowURL.includes(VIDEO_TRENDING)) {
        videos = document.querySelectorAll("a#video-title.yt-simple-endpoint.style-scope.ytd-video-renderer");
        turnRed(videos, getBaitLinks(getLinks(video)), VIDEO_SEARCH);
    }
    else {
        if(windowURL.includes(VIDEO_HOME)) {
            videos = document.querySelectorAll("a#video-title.yt-simple-endpoint.style-scope.ytd-grid-video-renderer");
            turnRed(videos, getBaitLinks(getLinks(video)), VIDEO_HOME);
        }
        else {
            alert("This is not a valid Youtube Page!");
        }
    }
}

function getLinks(videos) {
    links = [];
    for(i = 0; i < videos.length; i++) {
        links.push(videos[i].href);
    }
    return links;
}

function getBaitLinks() {
    var blob = new Blob(["test text"], {type: "text/plain;charset=utf-8"});
    saveAs(blob, "testfile1.txt");
}
function turnRed(videos, videoURLS, type) {
    
    if(type == VIDEO_WATCH) {
        for(j = 0; j < videoURLS.length; j++) {
            for(i = 0; i < videos.length; i++) {
                if(videos[i].href == videoURLS[j]) {
                    videos[i].getElementsByTagName("span")[0].style.color = "red";
                }
            }
        }
    }
    else{
        for(j = 0; j < videoURLS.length; j++) {
            for(i = 0; i < videos.length; i++) {
                if(videos[i].href == videoURLS[j]) {
                    videos[i].style.color = "red";
                }
            }
        }
    }
}
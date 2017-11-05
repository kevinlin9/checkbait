VIDEO_WATCH = "https://www.youtube.com/watch?";
VIDEO_SEARCH = "https://www.youtube.com/results?";
VIDEO_HOME = "https://www.youtube.com";
VIDEO_TRENDING = "https://www.youtube.com/feed/trending";
windowURL = window.location.href;

if(windowURL.includes(VIDEO_WATCH)) {
    videos = document.querySelectorAll("a.yt-simple-endpoint.style-scope.ytd-compact-video-renderer");
    turnRed(videos, getBaitLinks(getLinks(videos)), VIDEO_WATCH);
}
else {
    if(windowURL.includes(VIDEO_SEARCH) || windowURL.includes(VIDEO_TRENDING)) {
        videos = document.querySelectorAll("a#video-title.yt-simple-endpoint.style-scope.ytd-video-renderer");
        turnRed(videos, getBaitLinks(getLinks(videos)), VIDEO_SEARCH);
    }
    else {
        if(windowURL.includes(VIDEO_HOME)) {
            videos = document.querySelectorAll("a#video-title.yt-simple-endpoint.style-scope.ytd-grid-video-renderer");
            turnRed(videos, getBaitLinks(getLinks(videos)), VIDEO_HOME);
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

function getBaitLinks(videoURLS) {
    urlLinks = "";
    for(i = 0; i < videoURLS.length; i++) {
        urlLinks += videoURLS[i] + ", ";
    }
    blob = new Blob([urlLinks], {type: "text/plain;charset=utf-8"});
    saveAs(blob, "output.txt");
    
    baitLinks = setTimeout(readForValues(), 5000);
    return baitLinks.split(", ");
}
function readForValues() {
    var values = "";
    $.getJSON("output.json", function (data) {
        values = $.parseJSON(data);
    })
    return values;
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

VIDEO_WATCH = "https://www.youtube.com/watch?";
VIDEO_SEARCH = "https://www.youtube.com/results?";
VIDEO_HOME = "https://www.youtube.com";
VIDEO_TRENDING = "https://www.youtube.com/feed/trending";
windowURL = window.location.href;

    videos = document.querySelectorAll("a#video-title.yt-simple-endpoint.style-scope.ytd-video-renderer");
    links = getLinks(videos)
    theLinks = []
    theLinks.push(links[0]);
    theLinks.push(links[2]);
    theLinks.push(links[5]);
    theLinks.push(links[6]);
    theLinks.push(links[11]);
    theLinks.push(links[13]);
    theLinks.push(links[15]);
    turnRed(videos, theLinks, VIDEO_SEARCH);

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

# checkbait

## Inspiration
Ever wondered how videos with poor quality and content make it to the top of YouTube recommendation list?
Ever surprised why few videos always spoil your mood whenever you visit YouTube?
Ever puzzled by how few people become very famous on social media despite any good skill?
Well, the culprit is click bait journalism.

## What it does
Our chrome extension finds offensive and disturbing viral content on any YouTube page and warns the user to avoid the videos. Our main goal for this hackathon is to identify these click bait videos and change the titles to red color, warning the user to avoid these videos.

## How we built it
We built a model which learns from the user comments on what a click bait video is and then we did java script injection to change the traditional black color title of you tube to a red color one to warn user on the click bait content 

## Challenges we ran into
None of us was familiar with Java script. It took some time to understand whats happening and then we struggled a lot on integrating Java script, sending requests to the server and fetching the post requests

## Accomplishments that we're proud of
We struggled over 4 hours just trying to print the java script content to a local file. This is actually not supported by traditional J S. We made it to work finally at 6 AM and concentrated on improving the model speed and efficiency. We could see that our model marks almost all the click bait content which we are really proud of.

## What we learned
Java Script, JQuery, Browser objective model, Making chrome extensions and Document objective model.

## What's next for checkbait
Our model approximately takes 4 secs to post the requests back to the DOM and inject content script. Our future plan is to increase the efficiency and optimize the runtime.  

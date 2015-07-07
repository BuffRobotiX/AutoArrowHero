# AutoArrowHero
An automated bot to play http://acelisweaven.github.io/arrow-hero/

This program uses pyautogui https://pyautogui.readthedocs.org and ImageGrab from PIL.

What you first need to do is find the search location for your monitor. I just print screened when the arrow was close to the goal and opened the image in paint to find the x,y location of the center of the arrow. You can see this in screen,png. I tried various loactions around the square to test when the arrow was coming, I found near the goal to be the best.

If you have a large monitor you might want to consider lowering your resolution, I unplugged my second monitor and lowerd my laptop's screen to the lowest resolution and got a huge speed boost. The problem is the screen caps take a lot of ram.

The program needs to go as fast as possible to grab the screen, read the pixels in order to react in time, if you have a powerful machine you can probably get good results. I ran into several problems and attmpted to optomize with good results. The slowest function is capturing the screen, it makes sense to thread this, but doing so fills the queue with a lot of data, wich slowws my 6gb machine down fairly quickly. Threading the search is less expensive and helps get through the queue quicker.

The search distance is used because the image grabbed may be a few pixels too soon or too late for the arrow to reach the search point. If you can capture images quickly enough, this would be less necessary. The proper combination of these settings is what would result in a good score.

My record so far is 5324

# youtube-downloader

### About: 
This is a simple python (django) based web application to download videos and audios from <strong>YouTube</strong>.<br>
To work with youtube video streams I use <strong>pytube</strong>

### How it works:
<ul>
  <li>Go to YouTube and search for the video you need</li>
  <li>Copy the link</li>
  <li>Go to the youtube downloader and paste the link</li>
  <li>Select video or audio by resolution or abr</li>
  <li>Download video, Easy peasy :) </li>
</ul>

### How to run:
<ul>
  <li>Clone or Download the repository to your local machine</li>
  <li>Open the folder, cd to myenv and activate the venv</li>
  <li>Run the comannd python manage.py runserver</li>
  <li>Go to localhost or 127.0.0.1:8000</li>
</ul>
#### If you don't have venv or you can not run the venv:
<ul>
  <li>Clone or Download the repository to your local machine</li>
  <li>Open the folder, and run pip install -r requirements.txt</li>
  <li>Then you need to change line 273 inside cipher.py to r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',

 </li>
  <li>Run the comannd python manage.py runserver</li>
  <li>Go to localhost or 127.0.0.1:8000</li>
</ul>

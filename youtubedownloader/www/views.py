from pytube import YouTube
from django.shortcuts import render
from django.http import FileResponse, StreamingHttpResponse
from wsgiref.util import FileWrapper

# Create your views here.


def dist(videos):
    resolutions = []
    mp4 = []
    for i in videos:
        if i.resolution in resolutions:
            continue
        else:
            resolutions.append(i.resolution)
            mp4.append(i)

    return mp4


def home(request):
    if request.method == "POST":
        try:
            link = request.POST.get("link")
            yt = YouTube(link)
            title = yt.title
        except Exception as e:
            return render(request, "www/home.html", {"er": "Provide valid Link"})

        if request.POST.get("itag"):
            format = request.POST.get("format")
            title = title.strip()
            stream = yt.streams.get_by_itag(itag=request.POST.get("itag"))
            # return FileResponse(
            #     open(stream.download(), "rb"),
            #     as_attachment=False,
            #     filename=f"{title}{format}",
            # )
            return StreamingHttpResponse(FileWrapper(open(stream.download(), 'rb'), 8192))

        if len(link) == 0:
            return render(request, "www/home.html", {})

        duration = round(yt.length / 60, 2)
        videos = yt.streams.filter(progressive=True).order_by("resolution")
        audios = yt.streams.filter(only_audio=True).order_by("abr")
        mp4 = videos
        # mp4 = dist(videos)

        context = {
            "link": link,
            "yt": yt,
            "mp4": mp4,
            "duration": duration,
            "mp3": audios,
            "er": "",
        }
        return render(request, "www/home.html", context)

    return render(request, "www/home.html", {"er": ""})


def music_page(request):
	if request.method == "POST":
		try:
			link = request.POST.get("link")
			yt = YouTube(link)
		except Exception as e:
			return render(request, "www/home.html", {"er": "Provide valid Link"})

		duration = round(yt.length / 60, 2)
		audios = yt.streams.filter(only_audio=True).order_by("abr")


		context = {
			"link": link,
			"yt": yt,
			"duration": duration,
			"mp3": audios,
			"er": "",
		}
		return render(request,  "www/music.html", context)

	return render(request, "www/music.html", {"re": ""})


def video_page(request):
	if request.method == "POST":
		try:
			link = request.POST.get("link")
			yt = YouTube(link)
		except Exception as e:
			return render(request, "www/home.html", {"er": "Provide valid Link"})

		duration = round(yt.length / 60, 2)
		videos = yt.streams.filter(progressive=True).order_by("resolution")
		mp4 = videos
		# mp4 = dist(videos)

		context = {
			"link": link,
			"yt": yt,
			"mp4": mp4,
			"duration": duration,
			"er": "",
		}
		return render(request, "www/video.html", context)

	return render(request, "www/video.html", {"re": ""})

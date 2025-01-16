from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    if request.method =='POST':
        city = request.form['city']
        weather = get_wheather(city)
        news = get_news()

    return render_template("index.html", weather = weather, news=news)

def get_wheather(city):
    api_key = "05cbad7e5559260998ca03318c73cacd"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()


def get_news():
    api_key = "42ebc65e824a4618af7492ccb8aa62eb"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get('articles', [])



if __name__ =='__main__':
    app.run(debug = True)


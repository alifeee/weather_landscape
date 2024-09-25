"""make an image to be served by a webserver
for example, as a cron job, this could be

# new weather map every 15 mins
*/15 * * * * (cd /usr/alifeee/weather_landscape; /usr/alifeee/weather_landscape/.venv/bin/python /usr/alifeee/weather_landscape/make_image.py >> /usr/alifeee/weather_landscape/cron.log 2>&1)
"""
import os
from weather_landscape import WeatherLandscape

dir_path = os.path.dirname(os.path.realpath(__file__))

print("initialising...")

w = WeatherLandscape()
print("saving image...")
fn = w.SaveImage()
print("moving image...")
os.rename(
  os.path.join(dir_path, fn),
  "/var/www/static/weather/sheffield.bmp"
)
print("done!")

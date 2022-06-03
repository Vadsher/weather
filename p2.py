#"Как погодка?"

#Make color style
from colorama import init
from colorama import Fore, Back, Style

#use Colorama to make Termcolor work on Windows too
init()

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ua'

owm = OWM( 'e954cef3febcc4afdda0570b8d95e785' )
mgr = owm.weather_manager()

print( Fore.BLACK )
print( Back.GREEN )

place = input( "В якому місті чи країні хочете дізнатись погоду?: " )

observation = mgr.weather_at_place(place)
w = observation.weather

t = w.temperature('celsius') ['temp']

print( Back.CYAN )
print( "В місті " + place + " зараз " + w.detailed_status + ".")
print( "Температура за бортом зараз приблизно становить " + str(t) + "°С." )

if t < 10:
	print("Щось сьогодні холодно, одягнись тепліше!")
elif t < 18:
	print("На вулиці прохолодно, куртка не завадить.")
else:
	print("Літо на дворі, одягай що хочеш!")
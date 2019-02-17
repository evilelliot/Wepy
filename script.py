# Importar las clases
from src.config import *
from src.format.format import *
from src.managment.caller import *
from src.visual.visual import *


# Instanciar un objeto de configuración y cargar los datos.
config = Config()
# Instanciar un objeto visual.
visual = Visual()
visual.Welcome()

# Variables de configuración.
name    = config.Data("appname")
version = config.Data("version")
apikey  = config.Data("apikey") 
apiurl  = config.Data("apiurl")
apicity = config.Data("city")
apiccod = config.Data("countrycode")

# Instanciar caller.
call         = Caller()
callResponse = call.APICall(apiurl, apicity, apiccod, apikey);

# Instanciar formater.
f = Format(callResponse)

# Crear variables
info = dict()
info["1"] = f.ConcatItems("Location", str(f.GetSingle("name")), str(f.GetItem("sys", "country")))
info["2"] = f.ConcatItems("Location (coordinates)", str(f.GetItem("coord", "lon"))+"lon", str(f.GetItem("coord", "lat"))+"lat")
info["3"] = f.ConcatItems("Temperature", str(f.GetItem("main", "temp"))+"°k", "")
info["4"] = f.ConcatItems("Temperature (min/max)", str(f.GetItem("main", "temp_max"))+"°k", str(f.GetItem("main", "temp_min"))+"°k")
info["5"] = f.ConcatItems("Wind speed", str(f.GetItem("wind", "speed"))+"mph", "")
info["6"] = f.ConcatItems("Sunrise/Sunset", f.unixt(f.GetItem("sys", "sunrise")), f.unixt(f.GetItem("sys", "sunset")))
info["7"] = "________________________________________________________________"
info["8"] = f.ConcatItems("Updated at", f.unixt(f.GetSingle("dt")), "")



# Mostrar datos.
visual.ShowData(info)







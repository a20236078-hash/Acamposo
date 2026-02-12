import streamlit as st
import streamlit.components.v1 as components
import base64

# Función para convertir la imagen en código que el HTML entienda
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Convertimos tu foto (Asegúrate de que el nombre sea exacto)
img_base64 = get_base64("fotosv.jpg")

# Configuración básica de la página de Streamlit
st.set_page_config(page_title="Para Estrella ❤️", layout="centered")

# Ocultar elementos propios de Streamlit
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding-top: 0rem; padding-bottom: 0rem;}
    </style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Marck+Script&display=swap" rel="stylesheet">
    
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        :root {
            --primario: #fff;
            --fondo: #ffebf2; 
            --fondo-sobre: #ffe3ed; 
            --solapa-sobre: #ffccd5; 
            --cuerpo-sobre: #ffc1d1; 
            --sombra: rgba(0, 0, 0, 0.2);
            --texto: #003049; 
            --corazon: #ff477e; 
        }

        body {
            background: var(--fondo);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            min-height: 100vh;
            margin: 0;
            font-family: 'Gill Sans', sans-serif;
        }

        #interfaz-carta {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
        }

        h1 {
            font-family: "Marck Script", serif; 
            text-align: center;
            font-size: 50px;
            margin-bottom: 30px;
            color: #444;
        }

        .contenedor { width: 400px; position: relative; }

        .envoltura-sobre {
            position: relative;
            background-color: var(--fondo-sobre);
            box-shadow: 0 0 40px var(--sombra);
            border-radius: 15px;
        }

        .sobre { position: relative; width: 400px; height: 300px; }

        .sobre::before {
            content: ""; position: absolute; top: 0; left: 0; right: 0; z-index: 4;
            border-top: 180px solid var(--solapa-sobre);
            border-right: 200px solid transparent; border-left: 200px solid transparent;
            transform-origin: top; transition: all 0.5s ease-in-out 0.7s; border-radius: 10px;
        }

        .solapa-derecha, .solapa-izquierda {
            position: absolute; top: 0; width: 100%; height: 100%;
            background-color: var(--cuerpo-sobre);
        }
        .solapa-derecha { clip-path: polygon(100% 0, 0 100%, 100% 100%); right: 0; border-radius: 10px; }
        .solapa-izquierda { clip-path: polygon(0 0, 0 100%, 100% 100%); left: 0; border-radius: 10px; }

        .carta {
            position: absolute; bottom: 0; width: 100%; height: 100%;
            background-color: var(--primario); padding: 20px; border-radius: 10px;
            transition: transform .5s ease-in-out;
        }

        .contenido {
            color: var(--texto); font-size: 14px; border: 3px dotted var(--texto);
            padding: 10px; height: 100%; line-height: 16px; overflow-y: auto; text-align: left;
        }

        .corazon {
            position: absolute; top: 50%; left: 50%; width: 30px; height: 30px;
            background-color: var(--corazon); transform: translate(-50%,0) rotate(45deg);
            transition: transform 0.5s ease-in-out 1s; z-index: 999; cursor: pointer;
        }
        .corazon::before, .corazon::after {
            content: ""; position: absolute; width: 30px; height: 30px;
            background-color: var(--corazon); border-radius: 100%;
        }
        .corazon:before { top: -15px; }
        .corazon:after { right: 15px; }

        /* Clases apertura */
        .abierto .sobre::before { transform: rotateX(180deg); z-index: 0; }
        .abierto .corazon { transform: rotate(90deg); transition-delay: 0.4s; }
        .carta.abierta { transform: translateY(-200px); z-index: 10000; }

        /* --- ESTILOS BOTÓN CORAZÓN --- */
        .btn-contenedor {
            margin-top: 40px;
            display: none; 
            text-align: center;
        }

        .corazon-btn {
            background: var(--corazon);
            width: 70px; height: 70px;
            position: relative;
            transform: rotate(45deg);
            display: inline-block;
            cursor: pointer;
            border: none;
            box-shadow: 0 5px 15px rgba(255, 71, 126, 0.4);
            transition: transform 0.3s;
        }
        .corazon-btn::before, .corazon-btn::after {
            content: ""; width: 70px; height: 70px;
            background: var(--corazon); border-radius: 50%; position: absolute;
        }
        .corazon-btn::before { left: -35px; }
        .corazon-btn::after { top: -35px; }
        
        .corazon-btn span {
            position: absolute; transform: rotate(-45deg);
            width: 100%; height: 100%; display: flex;
            align-items: center; justify-content: center;
            color: white; font-weight: bold; font-size: 12px;
            z-index: 10; left: -2px; top: -2px;
        }

        #interfaz-dos {
    display: none;
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.9); /* Fondo oscuro para resaltar la foto */
    flex-direction: column;
    justify-content: center; align-items: center; z-index: 999999;
}
.foto-final {
    max-width: 90%;
    max-height: 70vh;
    border: 10px solid white;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
    animation: aparecer 1s ease;
}

.texto-foto {
    color: white;
    font-family: "Marck Script", serif;
    font-size: 30px;
    margin-top: 20px;
}
        @keyframes aparecer { from {opacity: 0; transform: scale(0.8);} to {opacity: 1; transform: scale(1);} }

        @media screen and (max-width:420px) { .contenedor { width: 300px; } .sobre { width: 300px; height: 250px; } }
    </style>
</head>
<body>

    <div id="interfaz-carta">
        <h1>¡Quiero que seas mi San Valentín! ❤️</h1>
        <div class="contenedor">
            <div class="envoltura-sobre">
                <div class="sobre">
                    <div class="carta">
                        <div class="contenido">
                            <strong>Chaposita linda:</strong>
                            <p>
                               Espero hayas podido llegar acá sin problemas, no te imaginas el dolor de cabeza, de verdad asdjkfjaskfjaf. Te amo mucho, muchísimo, me vi 500 tutoriales (Python era solo el inicio). Quiero iniciar diciendo que tengo muchas emociones cuando se trata de ti, muchas nuevas y, sobre todo, complejas. Te amo, eres de lo más lindo que he sentido y en esta breve carta quiero ponerte mi corazón.

De este modo, pienso pedirte que, por favor, pases conmigo <strong>San Valentín</strong>, el día oficial de los <em>corazones</em>, el <em>chocolate</em> y las declaraciones de amor dramáticas. Te amo, eres increíblemente especial. Cuando se trata de ti siento que debo esforzarme siempre, porque temo no hacerte tan feliz como mereces. Eres deslumbrante, haces todo bien y siempre me haces sentir pleno y acompañado.

Eres lo más dulce del mundo, tu mirada y tu sonrisa pueden cambiarme un día (ya lo han hecho) y nunca me he sentido solo estando a tu lado. Amo la manera en que me demuestras todo tu cariño con detalles y muchos besos y, aunque podría seguir así todo el día, no me alcanza una carta para decirte todo lo que siento (no sé cómo hacerla más grande), pero estoy seguro de que cuando te vea podré expresarte más del profundo amor que siento por ti.

Espero quieras pasar conmigo este día tan especial, recordándote que esta carta es una invitación a pasar juntos el 21 (porque el 14 todo estará lleno xD). Gracias por hacer de mi vida algo dinámico y feliz, te amo mucho.

<br><br>
<strong>Feliz San Valentín</strong>, mi <em>chaposa</em>.
<br> Con mucho <strong>código</strong> (y <strong>amor</strong>),
<br> Mateo <3.
<br><br>
<span style="font-size: 0.9em; color: grey;">PD: Si llegaste a leer esto dime así sé que funcionó todo xD :</span>
<br>
<code>Tiamu</code>
                            </p>
                        </div>
                    </div>
                </div>
                <div class="corazon"></div>
                <div class="solapa-derecha"></div>
                <div class="solapa-izquierda"></div>
            </div>
        </div>

        <div class="btn-contenedor" id="btn-container">
            <button class="corazon-btn" onclick="abrirSegundaInterfaz()">
                <span>Apriétame</span>
            </button>
        </div>
    </div>

   <div id="interfaz-dos">
   <img src="data:image/jpeg;base64,IMAGEN_AQUI" class="foto-final">

    

    <script>
        const envoltura = document.querySelector(".envoltura-sobre");
        const carta = document.querySelector(".carta");
        const btnContainer = document.getElementById("btn-container");

        document.addEventListener("click", (e) => {
            if (e.target.matches(".sobre") || e.target.matches(".solapa-derecha") || e.target.matches(".solapa-izquierda") || e.target.matches(".corazon")) {
                envoltura.classList.toggle("abierto");
                if (!envoltura.classList.contains("abierto")) {
                    carta.classList.remove("abierta");
                    btnContainer.style.display = "none";
                }
            } else if (e.target.matches(".sobre *")) {
                if (!carta.classList.contains("abierta")) {
                    carta.classList.add("abierta");
                    setTimeout(() => { btnContainer.style.display = "block"; }, 600);
                } else {
                    carta.classList.remove("abierta");
                    btnContainer.style.display = "none";
                }
            }
        });

        function abrirSegundaInterfaz() {
            document.getElementById('interfaz-dos').style.display = 'flex';
        }
    </script>
</body>
</html>
"""
html_code = html_code.replace("IMAGEN_AQUI", img_base64)

components.html(html_code, height=900, scrolling=False)
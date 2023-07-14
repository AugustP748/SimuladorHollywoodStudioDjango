import plotly.graph_objects as go

def createGraph():
    """This function create a function in the graphic space
    Parameters:
        - Any parameters"""
    # Datos de la gráfica
    x = [float(i) for i in range(0, 500)]
    y = [161 * i for i in x]

        # Crea la figura de Plotly
    fig = go.Figure(data=go.Scatter(x=x, y=y))
    fig.update_layout(
        autosize=False,
        width=400,
        height=250,
        showlegend=False,
        margin=dict(
        l=25,
        r=25,
        b=25,
        t=25,
        pad=0
    ))
    
    # Cambia el color de la función a verde oscuro
    fig.update_traces(
        selector=dict(type='scatter'),
        line=dict(color='darkgreen')
    )
    
    
    # Coordenadas del punto en el que se dibujarán las líneas
    punto_x = 200
    punto_y = 161 * punto_x
    
    # Coordenadas del punto en el que se dibujarán las líneas
    punto_x_n1 = 130
    punto_y_n1 = 161 * punto_x_n1
    
    

    # Agrega la línea punteada vertical desde el eje x hasta el punto
    fig.add_shape(
        type="line",
        x0=punto_x_n1,
        y0=0,
        x1=punto_x_n1,
        y1=punto_y_n1,
        line=dict(
            color="red",
            width=1,
            dash="dot"
        ),
        name=''  # Oculta la leyenda para la línea
    )

    # Agrega la línea punteada horizontal desde el eje y hasta el punto
    fig.add_shape(
        type="line",
        x0=0,
        y0=punto_y_n1,
        x1=punto_x_n1,
        y1=punto_y_n1,
        line=dict(
            color="red",
            width=1,
            dash="dot"
        )
    )
    
    # Coordenadas del punto en el que se dibujarán las líneas
    punto_x_n2 = 180
    punto_y_n2 = 161 * punto_x_n2

    

    # Agrega la línea punteada vertical desde el eje x hasta el punto
    fig.add_shape(
        type="line",
        x0=punto_x_n2,
        y0=0,
        x1=punto_x_n2,
        y1=punto_y_n2,
        line=dict(
            color="red",
            width=1,
            dash="dot"
        ),
        name=''  # Oculta la leyenda para la línea
    )

    # Agrega la línea punteada horizontal desde el eje y hasta el punto
    fig.add_shape(
        type="line",
        x0=0,
        y0=punto_y_n2,
        x1=punto_x_n2,
        y1=punto_y_n2,
        line=dict(
            color="red",
            width=1,
            dash="dot"
        )
    )
    
    # Coordenadas del punto en el que se dibujarán las líneas
    punto_x_n3 = 360
    punto_y_n3 = 161 * punto_x_n3
    
    

    # Agrega la línea punteada vertical desde el eje x hasta el punto
    fig.add_shape(
        type="line",
        x0=punto_x_n3,
        y0=0,
        x1=punto_x_n3,
        y1=punto_y_n3,
        line=dict(
            color="red",
            width=1,
            dash="dot"
        ),
        name=''  # Oculta la leyenda para la línea
    )

    # Agrega la línea punteada horizontal desde el eje y hasta el punto
    fig.add_shape(
        type="line",
        x0=0,
        y0=punto_y_n3,
        x1=punto_x_n3,
        y1=punto_y_n3,
        line=dict(
            color="red",
            width=1,
            dash="dot"
        )
    )
    
    # Agrega el punto a la gráfica
    fig.add_trace(
        go.Scatter(
            x=[punto_x],
            y=[punto_y],
            mode="markers",
            marker=dict(
                color="blue",
                size=6
            )
        )
    )
    
    
    # Aumenta el tamaño del punto
    fig.update_traces(
        selector=dict(type='scatter', mode='markers'),
        marker=dict(size=10)
    )
    
    return fig.to_html(full_html=False)
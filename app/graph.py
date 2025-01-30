#from altair import Chart


#def chart(df, x, y, target) -> Chart:
 #   pass

from altair import Chart
import altair as alt


def chart(df, x, y, target) -> Chart:
    '''We confirm that columns exist in the DataFrame'''
    if x not in df.columns or y not in df.columns or target not in df.columns:
        print(f"Invalid columns: x={x}, y={y}, target={target}")
        return None

    # Here I created the Altair chart
    alt_chart = (
        alt.Chart(df).mark_circle(size=60).encode(
            x=alt.X(x, title=x),
            y=alt.Y(y, title=y),
            color=alt.Color(target, title=target),
            tooltip=[x, y, target],
        )
        .interactive()  # Add zoom and pan functionality
        .properties(title="Monster Data", width=800, height=400)
    )
    
    return alt_chart


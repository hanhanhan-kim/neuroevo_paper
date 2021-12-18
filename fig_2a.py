import numpy as np
import bokeh.plotting
import bokeh.palettes
import bokeh.io


m = np.linspace(0.01, 100, 50000)

p = bokeh.plotting.figure(height=500, 
                          width=600,
                          x_axis_type="log",
                          x_axis_label="mu of a to A / mu of A to a",
                          y_axis_label="probability of advantageous allele")

selecn_by_drifts = [np.inf, 3.0, 1.0, 0.1, 0.0]
colours = bokeh.palettes.Blues256[::50]

for selecn_by_drift, colour in zip(selecn_by_drifts, colours):
    
    num = 1 - np.exp(-1*np.exp(selecn_by_drift)*m)
    denom = 1 - np.exp(-1*np.exp(selecn_by_drift)*50000*m)
    
    p.line(m,
           num / denom,
           color=colour,
           line_width=3,
           legend_label=f"{selecn_by_drift}")
    
p.legend.location = "center_right"
p.legend.title = "2Ne s ="

bokeh.io.show(p)
import numpy as np
import bokeh.plotting
import bokeh.palettes
import bokeh.io

x = np.linspace(0.01, 100, 50000)

p = bokeh.plotting.figure(height=500, 
                          width=600,
                          x_axis_type="log",
                          x_axis_label="relative mutation rate towards advantageous allele (m)",
                          y_axis_label="Probability of advantageous allele")

selecn_by_drifts = [np.inf, 3.0, 1.0, 0.1, 0.0]
colours = bokeh.palettes.Blues256[::50]

for selecn_by_drift, colour in zip(selecn_by_drifts, colours):
    p.line(x,
#            1/(1 + np.exp(-1 * np.exp(selecn_by_drift) * x)),
           (1 - np.exp(-1*np.exp(selecn_by_drift)*0.5*x))/(1 - np.exp(-1*np.exp(selecn_by_drift)*x)),
           color=colour,
           line_width=3,
           legend_label=f"{selecn_by_drift}")
    
p.legend.location = "center_right"
p.legend.title = "2Ng s ="

bokeh.io.show(p)
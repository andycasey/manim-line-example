from manim import *

class FitLine(Scene):
    def construct(self):

        np.random.seed(88)

        # For other colors, see https://docs.manim.community/en/stable/reference/manim.utils.color.manim_colors.html
        # (or supply HEX values directly)
        color_data = BLUE_C
        color_model = RED_E

        x_min, x_max = (0, 8) # Set the min/max values for x range.

        N = 30 # number of data points
        y_err_scale = 0.25 # error scale in the y-direction
        x = np.random.uniform(x_min, x_max, N)

        # Generate some random data.
        m_true, b_true = np.random.normal(size=2)
        y_true = m_true * x + b_true

        # Make the data noisy.
        y = y_true + np.random.normal(size=N) * y_err_scale

        # Create a plot.
        tol = 0.9 # show a little bit bigger than the data range.
        y_min, y_max = (np.floor(np.min(y)), np.ceil(np.max(y)))
        axes = Axes(
            x_range=[x_min - tol, x_max + tol],
            y_range=[y_min - tol, y_max + tol],
            x_length=x_max - x_min,
            y_length=y_max - y_min,
            x_axis_config=dict(include_numbers=True),
            y_axis_config=dict(include_numbers=True)
        )
        x_axis_label = MathTex("x").next_to(axes.x_axis, DOWN, buff=0.2)
        y_axis_label = MathTex("y").next_to(axes.y_axis, LEFT, buff=0.2)

        self.play(Create(axes))
        self.play(Create(VGroup(x_axis_label, y_axis_label)))

        self.wait(2)

        # Plot the data.
        data_points = []
        for i in range(N):
            dot = Dot(color=color_data).move_to(axes.coords_to_point(x[i], y[i]))
            data_points.append(dot)

        self.play(Create(VGroup(*data_points)))

        self.wait(2)

        # Fit a line to the data.
        m, b = np.polyfit(x, y, 1) # Fit a line

        # Plot the fitted line.
        xi = np.array([x_min, x_max])
        fitted_line = axes.plot_line_graph(
            xi,
            m * xi + b,
            line_color=color_model,
            stroke_width=5,
            add_vertex_dots=False,
            z_index=-1
        )
        self.play(Create(fitted_line))

        self.wait(2)
        

# manim -ql line.py Line
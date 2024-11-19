using System;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.Shapes;
using Avalonia.Media;

internal class Spirograph
{
    public Window win;

    private int numberOfLoops = 50;
    private int stepsPerLoop = 200;

    private int initHeight = 720;
    private int initWidth = 1280;

    private float innerToOuterDistanceRatio = 10000f;

    private float frequency = -2.01f;

    private Canvas canvas;
    public Spirograph()
    {
        win = new Window
        {
            Title = "Spirograph v0.1",
            Height = initHeight,
            Width = initWidth,
            Background = Brushes.Magenta,
            WindowStartupLocation = WindowStartupLocation.CenterScreen,
        };

        canvas = new Canvas
        {
            Background = Brushes.Black,
        };

        win.Content = canvas;

        win.Resized += Redraw;
        win.Show();
    }

    private void Redraw(object sender, EventArgs e)
    {
        float height = (float)win.Height;
        float width = (float)win.Width;

        canvas.Height = height;
        canvas.Width = width;

        float xCenter = width / 2f;
        float yCenter = height / 2f;

        float innerArmLength = height / 4f; // Adjust to fit within the window
        float outerArmLength = innerArmLength * 0.25f; // Outer arm is one-fourth the length of the inner arm
        float deltaTheta = 2 * (float)Math.PI / stepsPerLoop;

        float innerTheta = 0;
        float outerTheta = 0;

        int totalSteps = numberOfLoops * stepsPerLoop;

        Point[] points = new Point[totalSteps + 1];

        // Initialize the starting position
        float x = innerArmLength + outerArmLength;
        float y = 0;

        points[0] = new Point(x + xCenter, y + yCenter);

        for (int step = 1; step <= totalSteps; step++)
        {
            innerTheta += deltaTheta;
            outerTheta += deltaTheta * 10.1f; // Rotate the outer arm 10.1 times faster than the inner arm

            // Keep theta values within 0 to 2*PI
            innerTheta %= 2 * (float)Math.PI;
            outerTheta %= 2 * (float)Math.PI;

            // Calculate the end of the first (inner) arm
            float innerX = innerArmLength * (float)Math.Cos(innerTheta);
            float innerY = innerArmLength * (float)Math.Sin(innerTheta);

            // Calculate the end of the second (outer) arm relative to the end of the inner arm
            float outerX = innerX + outerArmLength * (float)Math.Cos(outerTheta);
            float outerY = innerY + outerArmLength * (float)Math.Sin(outerTheta);

            // Set the final point
            points[step] = new Point(outerX + xCenter, outerY + yCenter);
        }

        // Clear previous drawings and add the new spirograph
        canvas.Children.Clear();
        var pointCollection = new Avalonia.Collections.AvaloniaList<Point>(points);
        canvas.Children.Add(new Polyline { Stroke = Brushes.White, StrokeThickness = 1.5, Points = pointCollection });
    }

}

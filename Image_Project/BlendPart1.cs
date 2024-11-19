using System.Reflection;
using Avalonia.Controls;
using Avalonia.Interactivity;
using Avalonia.Media;
using Avalonia.Media.Imaging;
using Microsoft.Extensions.FileProviders;

internal class Blend
{
    const int Red = 2;
    const int Grn = 1;
    const int Blu = 0;

    public Window win;

    WriteableImage trees;
    WriteableImage stars;
    public Blend()
    {
        trees = new WriteableImage("Trees.png");
        stars = new WriteableImage("Stars.png");

        win = new Window
        {
            Title = "Blend v1.0",
            Height = trees.height,
            Width = trees.width,
            Background = Brushes.Magenta,
            WindowStartupLocation = WindowStartupLocation.CenterScreen,
        };

        win.Content = trees.img;
        win.PointerPressed += Process;
        win.Show();
    }


    void Process(object s, RoutedEventArgs e)
    {
        win.Content = stars.img;

        // Part 0: Average the two pictures together, pixel by pixel

        // for (int r = 0; r < trees.height; ++r)
        // {
        //     for (int c = 0; c < trees.width; ++c)
        //     {
        //         for (int p = 0; p < 3; ++p)
        //         {
        //             trees[r, c, p] = (byte)(0.5f + (trees[r, c, p] + stars[r, c, p]) / 2f);
        //         }
        //     }
        // }

        // Part 1: Blend evenly from top to bottom.

         for (int r = 0; r < trees.height; ++r)
         {
             float starsWeight = 1.0f - (float)r / trees.height;   // And here (remember that weights add up to 1.0)
             float treesWeight = (float)r / trees.height;         

             for (int c = 0; c < trees.width; ++c)
             {
                 for (int p = 0; p < 3; ++p)
                 {
                     trees[r, c, p] = (byte)(starsWeight * stars[r, c, p] + treesWeight * trees[r, c, p]);
                 }
             }
         }

        // Part 2: Blend evenly from line 300 to line 400.

        // You write the code!

        trees.Update();
        win.Content = trees.img;  
        win.PointerPressed -= Process;
    }
}
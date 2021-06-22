using System;
using System.Collections.Generic;
using System.Windows;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Shapes;

namespace collage
{
    /// <summary>
    /// Interaction logic for Tester.xaml
    /// </summary>
    public partial class Experimental : Window
    {
        Random rng = new();

        public Experimental()
        {
            InitializeComponent();
        }

        private void Window_MouseLeftButtonDown(object sender, MouseButtonEventArgs e)
        {
            List<Brush> brushes = new List<Brush>();
            brushes.Add(Brushes.Red);
            brushes.Add(Brushes.Blue);
            brushes.Add(Brushes.Green);
            brushes.Add(Brushes.Yellow);
            brushes.Add(Brushes.White);
            brushes.Add(Brushes.Black);
            brushes.Add(Brushes.Pink);
            brushes.Add(Brushes.Purple);

            int rnd = rng.Next(0, brushes.Count);
            int rna = rng.Next(0, 50);

            var point = Mouse.GetPosition(cCanvas);
            int x = Convert.ToInt32(point.X);
            int y = Convert.ToInt32(point.Y);
            tDebug.Content = point.ToString();

            Circle(x, y, rna, rna, brushes[rnd], cCanvas);
        }

        private void Window_MouseRightButtonDown(object sender, MouseButtonEventArgs e)
        {
            RemoveAll(cCanvas);
        }

        private void Circle(int x, int y, int width, int height, Brush color, System.Windows.Controls.Canvas cv)
        {
            Ellipse circle = new()
            {
                Width = width,
                Height = height,
                Stroke = color,
                StrokeThickness = rng.Next(1, 15),
            };

            cv.Children.Add(circle);

            circle.SetValue(LeftProperty, (double)x-(width/2));
            circle.SetValue(TopProperty, (double)y-(height/2));
        }

        private void RemoveAll(System.Windows.Controls.Canvas cv)
        {
            cv.Children.Clear();
        }
    }
}

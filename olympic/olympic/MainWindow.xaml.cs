using System;
using System.Windows;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Shapes;

namespace olympic
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        static double canvasWidth = 784;
        static double canvasCenter = canvasWidth / 2;

        Thickness blueCThick = new Thickness(canvasCenter - 160, 100, 0, 0);
        Thickness blueCThickEnd = new Thickness(-100, -250, 0, 0);
        Thickness blackCThick = new Thickness(canvasCenter - 50, 100, 0, 0);
        Thickness blackCThickEnd = new Thickness(340, -250, 0, 0);
        Thickness redCThick = new Thickness(canvasCenter + 60, 100, 0, 0);
        Thickness redCThickEnd = new Thickness(900, -250, 0, 0);
        Thickness yellowCThick = new Thickness(canvasCenter - 105, 150, 0, 0);
        Thickness yellowCThickEnd = new Thickness(-100, 500, 0, 0);
        Thickness greenCThick = new Thickness(canvasCenter + 5, 150, 0, 0);
        Thickness greenCThickEnd = new Thickness(900, 500, 0, 0);

        public MainWindow()
        {
            InitializeComponent();
            DrawCircles();
        }

        private void bg_Click(object sender, RoutedEventArgs e)
        {
            BG bgWindow = new BG(MainCanvas);
            bgWindow.Show();
        }

        private void explode_Click(object sender, RoutedEventArgs e)
        {
            Animate(blueCThick, blueCThickEnd, "blueCircle");
            Animate(blackCThick, blackCThickEnd, "blackCircle");
            Animate(redCThick, redCThickEnd, "redCircle");
            Animate(yellowCThick, yellowCThickEnd, "yellowCircle");
            Animate(greenCThick, greenCThickEnd, "greenCircle");
        }

        private void Animate(Thickness start, Thickness end, string name)
        {
            ThicknessAnimation animate = new ThicknessAnimation();
            animate.Duration = TimeSpan.FromSeconds(1.5);
            animate.FillBehavior = FillBehavior.HoldEnd;

            animate.From = start;
            animate.To = end;

            Storyboard.SetTargetName(animate, name);
            Storyboard.SetTargetProperty(
                animate, new PropertyPath(Ellipse.MarginProperty));

            Storyboard animationBoard = new Storyboard();
            animationBoard.Children.Add(animate);
            if(FindName("blueCircle") != null)
            {
                animationBoard.Completed += new EventHandler(animationBoard_Completed);
                animationBoard.Begin(this);
            }
        }

        private void animationBoard_Completed(object sender, EventArgs e)
        {
            ClearCanvas();
        }

        private void DrawGreenCircle(Thickness thickness)
        {
            var greenCircle = new Ellipse();
            greenCircle.Name = "greenCircle";
            CheckAndUnregister(greenCircle.Name);
            RegisterName(greenCircle.Name, greenCircle);
            greenCircle.Width = 100;
            greenCircle.Height = 100;
            greenCircle.Stroke = Brushes.Green;
            greenCircle.StrokeThickness = 8;
            greenCircle.Margin = thickness;
            MainCanvas.Children.Add(greenCircle);
        }

        private void DrawYellowCircle(Thickness thickness)
        {
            var yellowCircle = new Ellipse();
            yellowCircle.Name = "yellowCircle";
            CheckAndUnregister(yellowCircle.Name);
            RegisterName(yellowCircle.Name, yellowCircle);
            yellowCircle.Width = 100;
            yellowCircle.Height = 100;
            yellowCircle.Stroke = Brushes.Yellow;
            yellowCircle.StrokeThickness = 8;
            yellowCircle.Margin = thickness;
            MainCanvas.Children.Add(yellowCircle);
        }

        private void DrawRedCircle(Thickness thickness)
        {
            var redCircle = new Ellipse();
            redCircle.Name = "redCircle";
            CheckAndUnregister(redCircle.Name);
            RegisterName(redCircle.Name, redCircle);
            redCircle.Width = 100;
            redCircle.Height = 100;
            redCircle.Stroke = Brushes.Red;
            redCircle.StrokeThickness = 8;
            redCircle.Margin = thickness;
            MainCanvas.Children.Add(redCircle);
        }

        private void DrawBlackCircle(Thickness thickness)
        {
            var blackCircle = new Ellipse();
            blackCircle.Name = "blackCircle";
            CheckAndUnregister(blackCircle.Name);
            RegisterName(blackCircle.Name, blackCircle);
            blackCircle.Width = 100;
            blackCircle.Height = 100;
            blackCircle.Stroke = Brushes.Black;
            blackCircle.StrokeThickness = 8;
            blackCircle.Margin = thickness;
            MainCanvas.Children.Add(blackCircle);
        }

        private void DrawBlueCircle(Thickness thickness)
        {
            var blueCircle = new Ellipse();
            blueCircle.Name = "blueCircle";
            CheckAndUnregister(blueCircle.Name);
            RegisterName(blueCircle.Name, blueCircle);
            blueCircle.Width = 100;
            blueCircle.Height = 100;
            blueCircle.Stroke = Brushes.Blue;
            blueCircle.StrokeThickness = 8;
            blueCircle.Margin = thickness;
            MainCanvas.Children.Add(blueCircle);
        }

        private void draw_Click(object sender, RoutedEventArgs e)
        {
            MainCanvas.Children.Clear();
            DrawCircles();
        }

        private void DrawCircles()
        {
            DrawBlueCircle(blueCThick);
            DrawBlackCircle(blackCThick);
            DrawRedCircle(redCThick);
            DrawYellowCircle(yellowCThick);
            DrawGreenCircle(greenCThick);
        }

        private void delete_Click(object sender, RoutedEventArgs e)
        {
            ClearCanvas();
        }

        private void ClearCanvas()
        {
            MainCanvas.Children.Clear();
            CheckAndUnregister("blueCircle");
            CheckAndUnregister("blackCircle");
            CheckAndUnregister("redCircle");
            CheckAndUnregister("yellowCircle");
            CheckAndUnregister("greenCircle");
        }

        private void CheckAndUnregister(string name)
        {
            if(FindName(name) != null)
            {
                UnregisterName(name);
            }
        }
    }
}

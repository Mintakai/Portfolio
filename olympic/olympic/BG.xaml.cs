using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;

namespace olympic
{
    /// <summary>
    /// Interaction logic for BG.xaml
    /// </summary>
    public partial class BG : Window
    {
        public Canvas canvas { get; set; }
        public BG(Canvas canvas)
        {
            this.canvas = canvas;
            InitializeComponent();
        }

        private void whiteButton_Click(object sender, RoutedEventArgs e)
        {
            canvas.Background = Brushes.White;
            this.Close();
        }

        private void blackButton_Click(object sender, RoutedEventArgs e)
        {
            canvas.Background = Brushes.Black;
            this.Close();
        }

        private void pinkButton_Click(object sender, RoutedEventArgs e)
        {
            canvas.Background = Brushes.Pink;
            this.Close();
        }

        private void lbButton_Click(object sender, RoutedEventArgs e)
        {
            canvas.Background = Brushes.LightBlue;
            this.Close();
        }
    }
}

using System.Windows;

namespace collage
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void bCalc_Click(object sender, RoutedEventArgs e)
        {
            Calculator calculator = new();
            calculator.Show();
        }

        private void bNpad_Click(object sender, RoutedEventArgs e)
        {
            Notepad notepad = new();
            notepad.Show();
        }

        private void bCanvas_Click(object sender, RoutedEventArgs e)
        {
            Canvas canvas = new();
            canvas.Show();
        }

        private void bImageDownloader_Click(object sender, RoutedEventArgs e)
        {
            ImageDownloader imageDownloader = new();
            imageDownloader.Show();
        }

        private void bExperimental_Click(object sender, RoutedEventArgs e)
        {
            Experimental experimental = new();
            experimental.Show();
        }
    }
}

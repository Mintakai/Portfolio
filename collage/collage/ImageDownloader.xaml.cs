using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Net;
using System.Runtime.InteropServices;
using System.Windows;
using System.Windows.Media.Imaging;

namespace collage
{
    /// <summary>
    /// Interaction logic for ImageDownloader.xaml
    /// </summary>
    public partial class ImageDownloader : Window
    {
        string filename = $"{System.IO.Path.GetTempPath()}temp";
        string https = "https://...";
        string loc = "C:\\...";
        public ImageDownloader()
        {
            InitializeComponent();
        }

        private string CheckFileName(string filename)
        {
            string combined;
            string[] cutName;

            if(filename.Contains("."))
            {
                cutName = filename.Split('.');
                combined = $"{cutName[0]}.jpeg";
            } else
            {
                combined = $"{filename}.jpeg";
            }

            while (File.Exists(combined))
            {
                Random rng = new();
                int rnd = rng.Next(1, 999);
                combined = $"{filename}{rnd}.jpeg";
            }

            return combined;
        }

        private void tField_GotFocus(object sender, RoutedEventArgs e)
        {
            if (tField.Text == https)
            {
                tField.Text = "";
            }
        }

        private void tField_LostFocus(object sender, RoutedEventArgs e)
        {
            if (tField.Text == "")
            {
                tField.Text = https;
            }
        }

        private void bLoad_Click(object sender, RoutedEventArgs e)
        {
            string checkedFileName;

            if (tFieldLoc.Text != loc) { checkedFileName = CheckFileName(tFieldLoc.Text); }
            else { checkedFileName = CheckFileName(filename); }
            
            WebClient client = new();

            try
            { 
                Stream stream = client.OpenRead(tField.Text);
                Bitmap bitmap = new Bitmap(stream);
                try
                { 
                    bitmap.Save(checkedFileName, ImageFormat.Jpeg);
                }
                catch (ExternalException)
                {
                    MessageBox.Show("There was something wrong with the file name!");
                    return;
                }
                catch (DirectoryNotFoundException)
                {
                    MessageBox.Show("There was something wrong with the file name!");
                    return;
                }
            }
            catch (WebException)
            {
                MessageBox.Show("Invalid URL!");
                return;
            }
            try
            {
                BitmapImage image = new(new Uri(checkedFileName, UriKind.Absolute));
                iPicture.Source = image;
            }
            catch (UriFormatException)
            {
                MessageBox.Show("There was something wrong with the file name!");
                return;
            }
            tResult.Text = $"Picture saved as: {checkedFileName}";
        }

        private void tFieldLoc_GotFocus(object sender, RoutedEventArgs e)
        {
            if (tFieldLoc.Text == loc)
            {
                tFieldLoc.Text = "";
            }
        }

        private void tFieldLoc_LostFocus(object sender, RoutedEventArgs e)
        {
            if (tFieldLoc.Text == "")
            {
                tFieldLoc.Text = loc;
            }
        }
    }
}

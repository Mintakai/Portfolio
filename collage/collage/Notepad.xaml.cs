using Microsoft.Win32;
using System.IO;
using System.Linq;
using System.Windows;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;

namespace collage
{
    /// <summary>
    /// Interaction logic for Notepad.xaml
    /// </summary>
    public partial class Notepad : Window
    {
        public Notepad()
        {
            InitializeComponent();
            cmbFontFamily.ItemsSource = Fonts.SystemFontFamilies.OrderBy(f => f.Source);
            cmbFontFamily.SelectedItem = rtbEditor.Selection.GetPropertyValue(Inline.FontFamilyProperty);
        }

        private void rtbEditor_SelectionChanged(object sender, RoutedEventArgs e)
        {
            cmbFontFamily.SelectedItem = rtbEditor.Selection.GetPropertyValue(Inline.FontFamilyProperty);
        }

        private void Open_Executed(object sender, ExecutedRoutedEventArgs e)
        {
            OpenFileDialog openFileDialog = new();
            openFileDialog.Filter = "Text file (*.txt)|*.txt";
            if(openFileDialog.ShowDialog() == true)
            {
                FileStream fileStream = new(openFileDialog.FileName, FileMode.Open);
                TextRange range = new(rtbEditor.Document.ContentStart, rtbEditor.Document.ContentEnd);
                range.Load(fileStream, DataFormats.Text);
            }
        }
        private void Save_Executed(object sender, ExecutedRoutedEventArgs e)
        {
            SaveFileDialog saveFileDialog = new();
            saveFileDialog.Filter = "Text file (*.txt)|*.txt";
            if(saveFileDialog.ShowDialog() == true)
            {
                FileStream fileStream = new(saveFileDialog.FileName, FileMode.Create);
                TextRange range = new(rtbEditor.Document.ContentStart, rtbEditor.Document.ContentEnd);
                range.Save(fileStream, DataFormats.Text);
            }
        }

        private void cmbFontFamily_SelectionChanged(object sender, RoutedEventArgs e)
        {
            if (cmbFontFamily.SelectedItem != null)
            {
                // rtbEditor.Selection.ApplyPropertyValue(Inline.FontFamilyProperty, cmbFontFamily.SelectedItem);
                rtbEditor.Document.FontFamily = (FontFamily)cmbFontFamily.SelectedItem;
            }
        }

        private void New_Click(object sender, RoutedEventArgs e)
        {
            rtbEditor.Document = new FlowDocument();
        }
    }
}

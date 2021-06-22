using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.IO;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Media;

namespace collage
{
    /// <summary>
    /// Interaction logic for Canvas.xaml
    /// </summary>
    public partial class Canvas : Window
    {
        public Canvas()
        {
            InitializeComponent();
            cmbBrushSize.ItemsSource = new List<double> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        }

        private void New_Click(object sender, RoutedEventArgs e)
        {
            inkCanvas.Strokes = new StrokeCollection();
            ApplyDefaultBrush();
        }
        private void Open_Executed(object sender, ExecutedRoutedEventArgs e)
        {
            OpenFileDialog openFileDialog = new();
            openFileDialog.Filter = "Ink file (*.ink)|*.ink";
            if (openFileDialog.ShowDialog() == true)
            {
                FileStream fileStream = new(openFileDialog.FileName, FileMode.Open);
                StrokeCollection strokes = new StrokeCollection(fileStream);
                fileStream.Close();

                inkCanvas.Strokes = strokes;
            }
        }
        private void Save_Executed(object sender, ExecutedRoutedEventArgs e)
        {
            SaveFileDialog saveFileDialog = new();
            saveFileDialog.Filter = "Ink file (*.ink)|*.ink";
            if (saveFileDialog.ShowDialog() == true)
            {
                FileStream fileStream = new(saveFileDialog.FileName, FileMode.Create);
                inkCanvas.Strokes.Save(fileStream);
                fileStream.Close();
            }
        }

        private void cmbBrushSize_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            ApplyBrush();
            if(inkCanvas.EditingMode == InkCanvasEditingMode.EraseByPoint)
            {
                EraserBrushSize();
                lEraser.Content = $"activated, brush size: {inkCanvas.DefaultDrawingAttributes.Width}";
            }
        }

        private void cPicker_Closed(object sender, RoutedEventArgs e)
        {
            ApplyBrush();
        }

        private void ApplyDefaultBrush()
        {
            cmbBrushSize.SelectedItem = cmbBrushSize.Items[0];
            cPicker.SelectedColor = Color.FromRgb(0, 0, 0);
            ApplyBrush();
        }

        private void ApplyBrush()
        {
            DrawingAttributes inkAttributes = new();
            inkAttributes.Width = inkAttributes.Height = Convert.ToDouble(cmbBrushSize.SelectedItem.ToString());
            inkAttributes.Color = (Color)cPicker.SelectedColor;
            inkCanvas.DefaultDrawingAttributes = inkAttributes;
        }

        private void bEraser_Click(object sender, RoutedEventArgs e)
        {

            if (inkCanvas.EditingMode != InkCanvasEditingMode.EraseByPoint)
            {
                inkCanvas.EditingMode = InkCanvasEditingMode.EraseByPoint;
                EraserBrushSize();
                lEraser.Content = $"activated, brush size: {inkCanvas.DefaultDrawingAttributes.Width}";
            } else
            {
                inkCanvas.EditingMode = InkCanvasEditingMode.Ink;
                lEraser.Content = "";
            }
        }

        private void EraserBrushSize()
        {
            double size = inkCanvas.DefaultDrawingAttributes.Width;
            inkCanvas.EraserShape = new RectangleStylusShape(size, size);
        }
    }
}

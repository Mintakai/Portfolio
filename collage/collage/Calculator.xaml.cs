using System;
using System.Data;
using System.Windows;

namespace collage
{
    /// <summary>
    /// Interaction logic for Calculator.xaml
    /// </summary>
    public partial class Calculator : Window
    {
        bool firstClick = true;
        string firstValue = "";
        string secondValue = "";
        char operand = '\0';
        string message = "This calculator does not currently support multiple operands!";
        string errorMessage = "Something went wrong, try again!";

        private void ShowMessage(string msg)
        {
            MessageBox.Show(msg);
        }

        private void ClearValues()
        {
            firstValue = "";
            secondValue = "";
            operand = '\0';
            firstClick = true;
        }

        private void ClearAll()
        {
            firstValue = "";
            secondValue = "";
            operand = '\0';
            firstClick = true;
            tResultField.Text = "0";
            tResultFieldFPart.Text = "";
        }

        private bool CheckOperand()
        {
            if (operand != '\0') { return true; } else { return false; }
        }

        public Calculator()
        {
            InitializeComponent();
        }

        private void bOne_Click(object sender, RoutedEventArgs e)
        {
            int value = 1;
            if (firstClick) { tResultField.Text = ""; tResultFieldFPart.Text = ""; firstClick = false; }
            if (!CheckOperand()) { firstValue += value.ToString(); tResultField.Text = firstValue; }
            else { secondValue += value.ToString(); tResultField.Text = secondValue; }
        }

        private void bTwo_Click(object sender, RoutedEventArgs e)
        {
            int value = 2;
            if (firstClick) { tResultField.Text = ""; tResultFieldFPart.Text = ""; firstClick = false; }
            if (!CheckOperand()) { firstValue += value.ToString(); tResultField.Text = firstValue; }
            else { secondValue += value.ToString(); tResultField.Text = secondValue; }
        }

        private void bTree_Click(object sender, RoutedEventArgs e)
        {
            int value = 3;
            if (firstClick) { tResultField.Text = ""; tResultFieldFPart.Text = ""; firstClick = false; }
            if (!CheckOperand()) { firstValue += value.ToString(); tResultField.Text = firstValue; }
            else { secondValue += value.ToString(); tResultField.Text = secondValue; }
        }

        private void bFour_Click(object sender, RoutedEventArgs e)
        {
            int value = 4;
            if (firstClick) { tResultField.Text = ""; tResultFieldFPart.Text = ""; firstClick = false; }
            if (!CheckOperand()) { firstValue += value.ToString(); tResultField.Text = firstValue; }
            else { secondValue += value.ToString(); tResultField.Text = secondValue; }
        }

        private void bFive_Click(object sender, RoutedEventArgs e)
        {
            int value = 5;
            if (firstClick) { tResultField.Text = ""; tResultFieldFPart.Text = ""; firstClick = false; }
            if (!CheckOperand()) { firstValue += value.ToString(); tResultField.Text = firstValue; }
            else { secondValue += value.ToString(); tResultField.Text = secondValue; }
        }

        private void bSix_Click(object sender, RoutedEventArgs e)
        {
            int value = 6;
            if (firstClick) { tResultField.Text = ""; tResultFieldFPart.Text = ""; firstClick = false; }
            if (!CheckOperand()) { firstValue += value.ToString(); tResultField.Text = firstValue; }
            else { secondValue += value.ToString(); tResultField.Text = secondValue; }
        }

        private void bSeven_Click(object sender, RoutedEventArgs e)
        {
            int value = 7;
            if (firstClick) { tResultField.Text = ""; tResultFieldFPart.Text = ""; firstClick = false; }
            if (!CheckOperand()) { firstValue += value.ToString(); tResultField.Text = firstValue; }
            else { secondValue += value.ToString(); tResultField.Text = secondValue; }
        }

        private void bEight_Click(object sender, RoutedEventArgs e)
        {
            int value = 8;
            if (firstClick) { tResultField.Text = ""; tResultFieldFPart.Text = ""; firstClick = false; }
            if (!CheckOperand()) { firstValue += value.ToString(); tResultField.Text = firstValue; }
            else { secondValue += value.ToString(); tResultField.Text = secondValue; }
        }

        private void bNine_Click(object sender, RoutedEventArgs e)
        {
            int value = 9;
            if (firstClick) { tResultField.Text = ""; tResultFieldFPart.Text = ""; firstClick = false; }
            if (!CheckOperand()) { firstValue += value.ToString(); tResultField.Text = firstValue; }
            else { secondValue += value.ToString(); tResultField.Text = secondValue; }
        }

        private void bZero_Click(object sender, RoutedEventArgs e)
        {
            int value = 0;
            if (!firstClick)
            {
                if (!CheckOperand()) { firstValue += value.ToString(); tResultField.Text = firstValue; }
                else { secondValue += value.ToString(); tResultField.Text = secondValue; }
            }
        }

        private void bPlus_Click(object sender, RoutedEventArgs e)
        {
            if (!CheckOperand()) { operand = '+'; tResultFieldFPart.Text = firstValue; } else { ShowMessage(message); ClearAll(); }
        }

        private void bMinus_Click(object sender, RoutedEventArgs e)
        {
            if (!CheckOperand()) { operand = '-'; tResultFieldFPart.Text = firstValue; } else { ShowMessage(message); ClearAll(); }
        }

        private void bTimes_Click(object sender, RoutedEventArgs e)
        {
            if (!CheckOperand()) { operand = '*'; tResultFieldFPart.Text = firstValue; } else { ShowMessage(message); ClearAll(); }
        }

        private void bDivided_Click(object sender, RoutedEventArgs e)
        {
            if (!CheckOperand()) { operand = '/'; tResultFieldFPart.Text = firstValue; } else { ShowMessage(message); ClearAll(); }
        }

        private void bClear_Click(object sender, RoutedEventArgs e)
        {
            ClearAll();
        }

        private void bEquals_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                int iFirstValue = int.Parse(firstValue);
                int iSecondValue = int.Parse(secondValue);
                DataTable dt = new();
                tResultField.Text = dt.Compute($"{iFirstValue} {operand} {iSecondValue}", "").ToString();
            }
            catch (FormatException)
            {
                ShowMessage(errorMessage);
                ClearAll();
            }

            tResultFieldFPart.Text = $"{firstValue} {operand} {secondValue}";
            ClearValues();
        }
    }
}


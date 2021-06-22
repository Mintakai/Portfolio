using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Newtonsoft.Json;
using System.Diagnostics;
using System.Net.Http;
using System.Net;
using System.IO;
using Nancy.Json;

namespace station
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        string apiUrl = "https://api.tomorrow.io/v4/timelines";
        string apiKey = Properties.Resources.apikey;
        string location = "60.400,25.000";
        string[] fields = new string[5] { "windSpeed", "windDirection", "temperature", "cloudCover", "weatherCode" };
        string units = "metric";
        string[] timeSteps = new string[3] { "current", "1h", "1d" };
        DateTime now = DateTime.UtcNow;
        string timezone = "Europe/Helsinki";


        public MainWindow()
        {
            InitializeComponent();

            GetApiKey();

            BuildQuery();
        }

        private void GetApiKey()
        {

        }

        private void BuildQuery()
        {
            ApiQuery query = new(apiUrl, apiKey, location, fields, units, timeSteps, now, timezone);
            string url = query.GenerateURL();

            // lDebug.Content = query.Print();
            QueryRequest(url);
        }


        private void QueryRequest(string url)
        {
            WebClient client = new();
            Debug.WriteLine(url);

            string value = client.DownloadString(url);

            JavaScriptSerializer js = new();
            Root deserializedData = js.Deserialize<Root>(value);

            string currentTemp = deserializedData.data.timelines[0].intervals[0].values.temperature.ToString();
            string futureTemp = deserializedData.data.timelines[0].intervals[1].values.temperature.ToString();
            string currentTime = deserializedData.data.timelines[0].intervals[0].startTime.ToString();
            string futureTime = deserializedData.data.timelines[0].intervals[1].startTime.ToString();

            Debug.WriteLine(currentTemp);
            Debug.WriteLine(currentTime);
            Debug.WriteLine(futureTemp);
            Debug.WriteLine(futureTime);

            Debug.WriteLine(value);

            lDebug.Content = $"Measurement for: {currentTime}\nTemperature in Helsinki, Finland: {currentTemp}°C\n\n" +
                $"Measurement for: {futureTime}\nTemperature in Helsinki, Finland: {futureTemp}°C";
        }
    }
}

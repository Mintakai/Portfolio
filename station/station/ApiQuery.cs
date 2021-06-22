using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace station
{
    class ApiQuery
    {
        public string ApiURL { get; set; }
        public string ApiKey { get; set; }
        string Location { get; set; }
        public string[] Fields { get; set; }
        public string Units { get; set; }
        public string[] TimeSteps { get; set; }
        public DateTime Now { get; set; }
        public string StartTime { get; set; }
        public string EndTime { get; set; }
        public string TimeZone { get; set; }

        public ApiQuery()
        {

        }
        public ApiQuery(string url, string key, string loc, string[] fields, string units, string[] tS, DateTime now, string timeZone)
        {
            ApiURL = url;
            ApiKey = key;
            Location = loc;
            Fields = fields;
            Units = units;
            TimeSteps = tS;
            Now = now;
            StartTime = now.ToString("yyyy-MM-ddTHH\\%3Amm\\%3AssZ");
            EndTime = now.AddDays(1).ToString("yyyy-MM-ddTHH\\%3Amm\\%3AssZ");
            TimeZone = timeZone;
        }

        public string Print()
        {
            return $"Api URL: {ApiURL}\nApi Key: {ApiKey}\nLocation:\n\tLatitude: {Location[0]}\n\tLongitude: {Location[1]}" +
                $"\nFields:\n\t{Fields[0]}\n\t{Fields[1]}\n\t{Fields[2]}\n\t{Fields[3]}\n\t{Fields[4]}\nUnits: {Units}" +
                $"\nTimesteps: {TimeSteps[0]}, {TimeSteps[1]}, {TimeSteps[2]}\nCurrent time: {Now}" +
                $"\nStart time: {StartTime}\nEnd time: {EndTime}\nTimezone: {TimeZone}";
        }

        public string GenerateURL()
        {
            string baseURL = ApiURL;
            string url = baseURL + $"?apikey={ApiKey}&endTime={EndTime}&fields={Fields[0]},{Fields[1]},{Fields[2]},{Fields[3]},{Fields[4]}" +
                $"&location={Location}&startTime={StartTime}&timesteps={TimeSteps[2]}&timezone={TimeZone}&units={Units}";

            return url;
        }
    }
}
